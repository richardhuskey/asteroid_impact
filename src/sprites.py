# Asteroid Impact (c) Media Neuroscience Lab, Rene Weber
# Authored by Nick Winters
# 
# Asteroid Impact is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>. 
"""
AsteroidImpact game sprites including sprite-specific behaviors.
"""
from __future__ import absolute_import, division
import pygame
from resources import load_image, load_sound, NoneSound
import virtualdisplay
import math

class VirtualGameSprite(pygame.sprite.Sprite):
    """
    Sprite with higher resolution game position/size (gamerect) than on-screen
    position/size (rect)
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.gamerect = pygame.Rect(0, 0, 1, 1)

    def stop_audio(self):
        # override in derived classes
        pass

    def update_rect(self):
        self.rect = virtualdisplay.screenrect_from_gamerect(self.gamerect)


#classes for our game objects
class Cursor(VirtualGameSprite):
    """The Player's ship is moved around using the mouse cursor"""
    def __init__(self, game_bounds=virtualdisplay.screenplayarea):
        VirtualGameSprite.__init__(self) #call Sprite initializer
        # find screen diameter
        self.gamediameter = 32
        self.gamerect = pygame.Rect(0, 0, self.gamediameter,self.gamediameter)
        self.game_bounds = game_bounds
        self.update_rect()
        self.image = load_image(
            'cursor.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)

    def update(self, millis):
        """Move the cursor based on the mouse position"""
        pos = pygame.mouse.get_pos()

        # if the cursor is outside of the game area, move it back
        if not virtualdisplay.screenplayarea.collidepoint(pos):
            pos = (
                max(
                    min(pos[0], self.game_bounds.right),
                    self.game_bounds.left),
                max(
                    min(pos[1], self.game_bounds.bottom),
                    self.game_bounds.top))
            pygame.mouse.set_pos(pos)

        game_pos = virtualdisplay.gamepoint_from_screenpoint(pos)
        self.gamerect.center = game_pos
        self.update_rect()

class Target(VirtualGameSprite):
    """Targets (Crystals) don't move, but do play a sound when collected"""
    def __init__(self, diameter=32, left=20, top=20):
        VirtualGameSprite.__init__(self) #call Sprite initializer
        self.gamediameter = diameter
        self.gamerect = pygame.Rect(left, top, diameter, diameter)
        self.update_rect()
        self.image = load_image(
            'crystal.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)
        self.pickup_sound = load_sound('ring_inventory.wav')

    def stop_audio(self):
        self.pickup_sound.stop()

    def pickedup(self):
        """Play pick up sound"""
        self.pickup_sound.play()

    def update(self, millis):
        # hit test done in AsteroidImpactGameplayScreen
        pass


def map_range(value, from_low, from_high, to_low, to_high):
    'return value in range [from_low, from_high] mapped to range [to_low, to_high]'
    return to_low + (to_high-to_low)*(value-from_low)/(from_high - from_low)
def clamp_range(value, limit_low, limit_high):
    'return limit_low if value < limit_low, limit_high if value > limit_high, otherwise value'
    if (value < limit_low): return limit_low
    if (limit_high < value): return limit_high
    return value

class Asteroid(VirtualGameSprite):
    """Asteroids move in straight lines, bouncing off the edges of the game play area"""
    def __init__(self, diameter=200, dx=4, dy=10, left=20, top=20, area=None):
        VirtualGameSprite.__init__(self) #call Sprite intializer
        self.gamediameter = diameter
        self.gamerect = pygame.Rect(left, top, diameter, diameter)
        self.update_rect()
        self.image = load_image(
            'asteroid.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)

        if area:
            self.GAME_PLAY_AREA = area
        else:
            self.GAME_PLAY_AREA = virtualdisplay.GAME_PLAY_AREA
        # rect uses integer positions but I need to handle fractional pixel/frame speeds.
        # store float x/y positions here:
        self.gametopfloat = float(top)
        self.gameleftfloat = float(left)
        self.dx = dx
        self.dy = dy
        self.speedfactor = 1.0
        self.gamediameternew_start_diameter = diameter
        self.gamediameternew_end_diameter = diameter
        self.gamediameternew_transition_duration_millis = 0
        self.gamediameternew_transition_remaining_millis = 0
        self.dxnew = self.dx
        self.dynew = self.dy

    def copy_from(self, asteroid):
        self.gamediameter = asteroid.gamediameter
        self.gamerect = asteroid.gamerect.copy()
        self.update_rect()
        self.image = load_image(
            'asteroid.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)
        self.GAME_PLAY_AREA = asteroid.GAME_PLAY_AREA
        self.gametopfloat = asteroid.gametopfloat
        self.gameleftfloat = asteroid.gameleftfloat
        self.dx = asteroid.dx
        self.dy = asteroid.dy
        self.gamediameternew_start_diameter = asteroid.gamediameter
        self.gamediameternew_end_diameter = asteroid.gamediameter
        self.gamediameternew_transition_duration_millis = 0
        self.gamediameternew_transition_remaining_millis = 0
        self.dxnew = self.dx
        self.dynew = self.dy

    def update(self, millis):
        """Update the position and direction of the Asteroid to move, and bounce"""

        # handle size transition:
        if (self.gamediameternew_transition_remaining_millis > 0):
            self.gamediameternew_transition_remaining_millis -= millis
            if (self.gamediameternew_transition_remaining_millis < 0):
                self.gamediameternew_transition_remaining_millis = 0

            # Transition diameter
            newdiameter = int(round(
                map_range(self.gamediameternew_transition_remaining_millis,
                    self.gamediameternew_transition_duration_millis,
                    0,
                    self.gamediameternew_start_diameter,
                    self.gamediameternew_end_diameter)))

            center = self.gamerect.center
            if (newdiameter != self.gamediameter):
                self.gamediameter = newdiameter
                self.gamerect.size = (newdiameter, newdiameter)
                self.gamerect.center = center
                self.update_rect()
                # resample image
                #TODO: is this too slow?
                # Yep, until the images are cached this is super slow
                self.image = load_image(
                    'asteroid.png',
                    (self.rect.width, self.rect.height),
                    convert_alpha=True)

        # when bouncing, change from expected X or Y speed towards 
        # new speed by at most +/-4px/frame
        adjusted_abs_dx = clamp_range(abs(self.dxnew), max(abs(self.dx)-4,1), abs(self.dx)+4)
        adjusted_abs_dy = clamp_range(abs(self.dynew), max(abs(self.dy)-4,1), abs(self.dy)+4)
        
        # bounce by setting sign of x or y speed if off of corresponding side of screen
        if self.gamerect.left < self.GAME_PLAY_AREA.left:
            self.dx = adjusted_abs_dx
        if  self.gamerect.right > self.GAME_PLAY_AREA.right:
            self.dx = -adjusted_abs_dx
        if self.gamerect.top < self.GAME_PLAY_AREA.top:
            self.dy = adjusted_abs_dy
        if self.gamerect.bottom > self.GAME_PLAY_AREA.bottom:
            self.dy = -adjusted_abs_dy

        self.gameleftfloat += self.dx * self.speedfactor
        self.gametopfloat += self.dy * self.speedfactor
        self.gamerect.left = self.gameleftfloat
        self.gamerect.top = self.gametopfloat
        self.update_rect()

class BasePowerup(VirtualGameSprite):
    """Base class for power-ups so they share common expiration behavior"""
    def __init__(self, diameter=16, left=50, top=50, maxduration=5.0):
        VirtualGameSprite.__init__(self) #call Sprite initializer
        self.gamediameter = diameter
        # likely overwritten in derived class:
        self.gamerect = pygame.Rect(left, top, diameter, diameter)
        self.update_rect()

        self.maxduration = maxduration # seconds
        self.active = False
        self.duration = 0

        self.used = False

    def update(self, millis, frame_outbound_triggers, cursor, asteroids):
        """Deactivate power-up if duration has expired"""
        if self.active:
            self.duration += millis / 1000.

            if self.duration > self.maxduration:
                # deactivate:
                self.deactivate(cursor, asteroids)

    def activate(self, *args):
        """Activate power-up because it was picked up"""
        self.oldgamerect = self.gamerect.copy()
        self.active = True
        self.duration = 0
        self.used = False

    def deactivate(self, cursor, asteroids):
        """Deactivate power-up"""
        self.active = False
        self.gamerect = self.oldgamerect
        self.update_rect()
        self.used = True
        self.kill()

class SlowPowerup(BasePowerup):
    """While active, the SlowPowerup slows the asteroids to a crawl"""
    def __init__(self, diameter=32, left=100, top=100):
        BasePowerup.__init__(self, diameter=diameter, left=left, top=top, maxduration=5.0)
        self.type = 'slow'
        self.gamerect = pygame.Rect(left, top, diameter, diameter)
        self.update_rect()
        self.image = load_image(
            'clock.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)

        self.sound_begin = load_sound('slow start.wav')
        self.sound_end = load_sound('slow end.wav')
        # these let me start the ending sound to end overlapping when the effect ends:
        self.sound_end_duration = self.sound_end.get_length() - 0.5
        self.sound_end_started = False

        self.speedfactor = 0.25

    def stop_audio(self):
        self.sound_end.stop()
        self.sound_begin.stop()

    def update(self, millis, frame_outbound_triggers, cursor, asteroids):
        """ Play effect end sound if due"""
        BasePowerup.update(self, millis, frame_outbound_triggers, cursor, asteroids)

        if self.active:
            # start the end effect sound to end when powerup ends:
            if (self.maxduration - self.duration < self.sound_end_duration
                    and not self.sound_end_started):
                self.sound_end_started = True
                self.sound_end.play()
            for asteroid in asteroids:
                asteroid.speedfactor = self.speedfactor

    def activate(self, cursor, asteroids, *args):
        """Play start sound. Slow asteroids to a crawl"""
        BasePowerup.activate(self, *args)

        # adjust speed of asteroids
        for asteroid in asteroids:
            asteroid.speedfactor = self.speedfactor

        # disappear offscreen
        self.gamerect.top = -10000
        self.gamerect.left = -10000
        self.update_rect()

        self.sound_begin.play()

        self.sound_end_started = False

    def deactivate(self, cursor, asteroids):
        """Restore normal speed of asteroids"""
        BasePowerup.deactivate(self, cursor, asteroids)

        # restore speed of asteroids
        for asteroid in asteroids:
            asteroid.speedfactor = 1.0

class ShieldPowerup(BasePowerup):
    """
    While active, the ShieldPowerup prevents the player from dying due to
    collisions with asteroids.
    """
    def __init__(self, diameter=32, left=80, top=80):
        BasePowerup.__init__(self, diameter=diameter, left=left, top=top, maxduration=5.0)
        self.type = 'shield'
        self.gamerect = pygame.Rect(left, top, diameter, diameter)
        self.update_rect()
        self.image = load_image(
            'shield.png',
            (self.rect.width, self.rect.height),
            convert_alpha=True)
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))

        self.sound_begin = load_sound('shield start.wav')
        self.sound_end = load_sound('shield end.wav')
        # these let me start the ending sound to end overlapping when the effect ends:
        self.sound_end_duration = self.sound_end.get_length() - 1.0
        self.sound_end_started = False

    def stop_audio(self):
        self.sound_begin.stop()
        self.sound_end.stop()

    def activate(self, cursor, asteroids, *args):
        """Play activation sound"""
        BasePowerup.activate(self, *args)

        self.sound_begin.play()

        self.sound_end_started = False

    def update(self, millis, frame_outbound_triggers, cursor, asteroids):
        """Follow cursor. Play effect end sound if due"""
        BasePowerup.update(self, millis, frame_outbound_triggers, cursor, asteroids)
        if self.active:
            # follow on top of cursor:
            self.gamerect.center = cursor.gamerect.center
            self.update_rect()

            # "ignore collisions" logic happens in Game Screen

            # start the end effect sound to end when powerup ends:
            if (self.maxduration - self.duration < self.sound_end_duration
                    and not self.sound_end_started):
                self.sound_end_started = True
                self.sound_end.play()

class NonePowerup(BasePowerup):
    """This power-up has no effect except delaying the next power-up from spawning"""
    def __init__(self, duration=10.0):
        # configure as a circle completely covering the screen so I get picked up
        # as soon as available
        diameter = 10*virtualdisplay.GAME_PLAY_AREA.width
        self.gamerect = pygame.Rect(0,0, diameter, diameter)
        self.gamerect.centerx = virtualdisplay.GAME_PLAY_AREA.width//2
        self.gamerect.centery = virtualdisplay.GAME_PLAY_AREA.height//2
        BasePowerup.__init__(
            self,
            diameter=diameter,
            left=self.gamerect.left,
            top=self.gamerect.top,
            maxduration=duration)
        self.type = 'none'
        self.image = None
        self.update_rect()

class ReactionTimePrompt(VirtualGameSprite):
    """Game element to test reaction time"""
    def __init__(
            self,
            diameter=64,
            left=20,
            top=20,
            sound='tone440.wav',
            image='triangle.png',
            input_type='key',
            input_key='K_1',
            showtimes_millis=[],
            showtimes_trigger_counts=[],
            timeout_millis = 1000,
            **kwargs_extra):
        #if kwargs_extra: print 'extra arguments:', kwargs_extra
        VirtualGameSprite.__init__(self) #call Sprite initializer
        self.gamediameter = diameter
        self.gamerect_visible = pygame.Rect(left, top, diameter, diameter)
        self.gamerect_hidden = pygame.Rect(-9999, -9999, diameter, diameter)
        self.gamerect = self.gamerect_hidden
        self.update_rect()

        if not image or image == 'none':
            image = 'transparent.png'
        self.image = load_image(
            image,
            (self.rect.width, self.rect.height),
            convert_alpha=True)
        
        if sound and sound != 'none':
            self.prompt_sound = load_sound(sound)
        else:
            self.prompt_sound = NoneSound()

        self.showtimes_millis = showtimes_millis
        # todo: implement trigger showing
        self.showtimes_trigger_counts = showtimes_trigger_counts
        self.timeout_millis = timeout_millis
        self.visible = False
        self.total_elapsed = 0
        self.showtime_last = 0 # millis when shown
        self.step_trigger_count_last = 0
        if input_type == 'key':
            pygame_key_constant = getattr(pygame, input_key, None)
            if not pygame_key_constant:
                print 'input_key of "%s" not found. Please use one of the following'%input_key
                print ', '.join(['"'+s+'"' for s in dir(pygame) if s.startswith('K_')])
                raise QuitGame
            self.dismiss_test = lambda evt: evt.type == pygame.KEYDOWN and evt.key == pygame_key_constant
        else:
            # TODO: allow specifying something other than left mouse
            self.dismiss_test = lambda evt: evt.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]

    def stop_audio(self):
        self.prompt_sound.stop()

    def activate(self):
        self.gamerect = self.gamerect_visible
        self.update_rect()
        self.visible = True
        self.prompt_sound.play()

    def deactivate(self):
        self.gamerect = self.gamerect_hidden
        self.update_rect()
        self.visible = False
        # fadeout avoids "click" at end, but I wish I could do shorter duration
        self.prompt_sound.fadeout(100)

    def update(self, millis, logrowdetails, frame_outbound_triggers, events, step_trigger_count):
        old_total_elapsed = self.total_elapsed
        self.total_elapsed += millis

        if not self.visible:
            for showtime in self.showtimes_millis:
                if (old_total_elapsed < showtime and
                    showtime <= self.total_elapsed):
                    # show
                    self.showtime_last = self.total_elapsed
                    self.activate()
            if (not self.visible 
                and self.step_trigger_count_last != step_trigger_count
                and self.showtimes_trigger_counts
                and step_trigger_count in self.showtimes_trigger_counts):
                    # show
                    self.showtime_last = self.total_elapsed
                    self.activate()
        else:
            visible_ms = self.total_elapsed - self.showtime_last
            logrowdetails['reaction_prompt_state'] = 'waiting'
            logrowdetails['reaction_prompt_millis'] = visible_ms
            # showing now
            if self.showtime_last + self.timeout_millis <= self.total_elapsed:
                # timed out. Hide
                self.deactivate()
                logrowdetails['reaction_prompt_state'] = 'timeout'
                logrowdetails['reaction_prompt_millis'] = visible_ms

            for event in events:
                if self.dismiss_test(event):
                    logrowdetails['reaction_prompt_state'] = 'complete'
                    logrowdetails['reaction_prompt_millis'] = visible_ms
                    # correct key pressed
                    self.deactivate()

        self.step_trigger_count_last = step_trigger_count
