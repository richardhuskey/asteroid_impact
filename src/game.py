# Asteroid Impact (c) Media Neuroscience Lab, Rene Weber
# Authored by Nick Winters
# 
# Asteroid Impact is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>. 
"""
Game loop and screen management for Asteroid Impact game.
"""

# to make python3 porting easier:
# see http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
from __future__ import absolute_import, division
#>>> 6 / 7
#1
#>>> from __future__ import division
#>>> 6 / 7
#1.2857142857142858


import argparse
import os
from os import path
import json
import pygame
from pygame.locals import *

import sys

try:
    import serial
except ImportError as e:
    print e
    print 'install pyserial, typicially by running `pip install pyserial`'
    print 'otherwise, see https://pypi.python.org/pypi/pyserial'
    import sys
    sys.exit(1)


if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'

from screens import (
    AsteroidImpactInstructionsScreen,
    UserTextScreen,
    SurveyQuestionScreen,
    AsteroidImpactGameplayScreen,
    AsteroidImpactInfiniteGameplayScreen,
    BlackScreen,
    ParallelPortTestScreen,
    QuitGame)
import resources
from sprites import Target
import virtualdisplay
from logger import AsteroidLogger

# command-line arguments:
parser = argparse.ArgumentParser(description='Run Asteroid Impact game.')
parser.add_argument('--music-volume', type=float, default=1.0,
                    help='Music volume, 1.0 for full.')
parser.add_argument('--effects-volume', type=float, default=1.0,
                    help='Sound effects volume, 1.0 for full.')
parser.add_argument('--display-width', type=int, default=640,
                    help='Width of window or full screen mode.')
parser.add_argument('--display-height', type=int, default=480,
                    help='Height of window or full screen mode.')
parser.add_argument('--window-x', type=int, default=None,
                    help='X position of window.')
parser.add_argument('--window-y', type=int, default=None,
                    help='Y position of window.')
parser.add_argument('--display-mode', choices=['windowed', 'fullscreen'],
                    default='windowed',
                    help='Whether to run windowed or fullscreen.')
parser.add_argument('--list-modes', default=False, const=True, nargs='?',
                    help='List available full screen display modes and exit.')
parser.add_argument('--script-json', type=str, default=None,
                    help=('script.json file listing all steps such as instructions, ' +
                          'gameplay (with levels) and black screens. See ' +
                          'samplescript.json for example.'))
parser.add_argument('--levels-json', type=str, default=None,
                    help=('levellist.json file listing all levels to complete. Ignored ' +
                          'when specifying --script-json'))
parser.add_argument('--single-level-json', type=str, default=None,
                    help=('level.json file to test a single level. Ignored when ' +
                          'specifying --script-json'))
parser.add_argument('--subject-number', type=str, default='',
                    help='Subject number to include in log.')
parser.add_argument('--subject-run', type=str, default='',
                    help='Subject run number to include in the log.')
parser.add_argument('--log-filename', type=str, default=None,
                    help='File to save log CSV file to with per-frame data.')
parser.add_argument('--log-overwrite', choices=['true', 'false'], default='false',
                    help='Whether to overwrite pre-existing log file.')
parser.add_argument('--trigger-blink', choices=['true', 'false'], default='false',
                    help='Blink sprite on screen when trigger pulse is received.')
parser.add_argument('--parallel-test-address', type=str, default=None,
                    help='Launch parallel port test interface with specified parallel port data address.')


class GameModeManager(object):
    """
    Follow the instructions to switch between game screens, and levels
    Rather than specifying a single level list, specify a file that has a list of entries
    where each entry specifies the following:

     * Action: Either Instructions, Game, or Black Screen
     * Levels: For the game, the list of level files to play. The player will progress (or
       not) through them in order, and after completing the last level will start again at
       the beginning. Dying will restart the current level.
     * Duration: After this many seconds move to the next step, regardless of what the
       player is doing now.
    """
    def __init__(self, args):
        self.args = args
        # assume error happened if we didn't reach end of __init__
        self.skipgame = True

        self.max_asteroid_count = 12

        if self.args.script_json != None:
            with open(self.args.script_json) as f:
                self.script_json = json.load(f)
                
                # allow script_json to be list of steps
                # or object with 'steps' attribute
                if isinstance(self.script_json, list):
                    self.gamesteps = self.script_json
                    self.script_json = dict(steps=self.gamesteps)
                else:
                    self.gamesteps = self.script_json['steps']
                
            if self.args.levels_json != None or self.args.single_level_json != None:
                print ('Error: When specifying script json you must specify levels in ' +
                       'script, not command-line argument.')
                return
        else:
            levelsjson = 'levels/standardlevels.json'
            if self.args.levels_json != None:
                if not path.exists(self.args.levels_json):
                    print 'Error: Could not find file at "%s"'%self.args.levels_json
                    return
                elif self.args.single_level_json != None:
                    print 'Error: Invalid arguments. Do not specify both --levels-json and --single-level-json'
                    return
                else:
                    levelsjson = self.args.levels_json
            elif self.args.single_level_json != None:
                levelsjson = [self.args.single_level_json]

            # use these steps when the steps aren't specified on the console:
            self.gamesteps = [
                dict(action='instructions',
                     duration=None),
                dict(action='game',
                     levels=levelsjson,
                     duration=None)]
            self.script_json = dict(steps=self.gamesteps)
        
        # load/validate trigger options:
        self.trigger_enabled = False
        self.trigger_key = None
        self.trigger_serialport = None
        self.trigger_serialport_byte_value = None
        if self.script_json.has_key('trigger_settings'):
            trigger_settings = self.script_json['trigger_settings']
            if trigger_settings['mode'] == 'keyboard':
                self.trigger_enabled = True
                keyboard_settings = trigger_settings['keyboard_options']
                self.trigger_key = getattr(pygame, keyboard_settings['trigger_key'], None)
                if not self.trigger_key:
                    print 'trigger_key not found. Please use one of the following'
                    print ', '.join(['"'+s+'"' for s in dir(pygame) if s.startswith('K_')])
                    return
            elif trigger_settings['mode'] == 'serial':
                self.trigger_enabled = True
                serial_settings = trigger_settings['serial_options']
                
                if not serial_settings.has_key('trigger_byte_value'):
                    print('for serial port, serial_options needs a trigger_byte_value '+
                          'attribute whose value is the value of the character sent over'+
                          'serial, such as 53 for Ascii "5"')
                self.trigger_serialport_byte_value = int(serial_settings['trigger_byte_value'])
                
                serialport_options = dict(
                    port=serial_settings['port'],
                    timeout=0.0,
                    baudrate=19200)

                if serial_settings.has_key('bytesize'):
                    serialport_options['bytesize'] = int(serial_settings['bytesize'])
                if serial_settings.has_key('stopbits'):
                    serialport_options['stopbits'] = int(serial_settings['stopbits'])
                if serial_settings.has_key('parity'):
                    parity_options = dict(
                        even=serial.PARITY_EVEN,
                        mark=serial.PARITY_MARK,
                        names=serial.PARITY_NAMES,
                        none=serial.PARITY_NONE,
                        odd=serial.PARITY_ODD,
                        space=serial.PARITY_SPACE)
                    # convert parity option
                    if parity_options.has_key(serial_settings['parity']):
                        serialport_options['parity'] = parity_options[serial_settings['parity']]
                    else:
                        print ('serial_options parity value of "' + serial_settings['parity']
                            + '" was not one of the expected values: ' + json.dumps(parity_options.keys()))
                        return
                        
                try:
                    print 'opening serialport with options:', serialport_options
                    self.trigger_serialport = serial.Serial(**serialport_options)
                except serial.SerialException as e:
                    print 'could not open configured serial port'
                    print e
                    print 'exiting.'
                    # exit
                    return

                
                # try opening serial port and loading remaining settings
            elif trigger_settings['mode'] == 'none':
                self.trigger_enabled = False
            else:
                print 'trigger_settings mode of "' + trigger_settings['mode'] + '" should be one of keyboard, serial or none'
                return
        
        if self.args.parallel_test_address:
            # try to parse parallel port address
            pport_debug_addr = int(self.args.parallel_test_address, 16)
            
            # ignore step list and replace with just parallel port test step
            self.gamesteps = [
                dict(action='parallel_port_test',
                     parallel_test_address=pport_debug_addr,
                     duration=None)]


        # validate steps and load levels:
        for i, step in enumerate(self.gamesteps):
            # duration must be not specified, none or float
            if step.has_key('duration'):
                if step['duration'] != None:
                    step['duration'] = float(step['duration'])
            else:
                step['duration'] = None

            if step.has_key('trigger_count'):
                if step['trigger_count'] != None:
                    step['trigger_count'] = int(step['trigger_count'])
            else:
                step['trigger_count'] = None

            # reaction_prompts
            if (step.has_key('reaction_prompts')
                    and step['reaction_prompts'] != None
                    and len(step['reaction_prompts']) > 0):
                # todo: verify/cleanup each reaction_prompt entry
                pass
            else:
                step['reaction_prompts'] = None

                
            if step['action'] == 'instructions':
                # nothing extra to validate
                pass
            elif step['action'] == 'text':
                # 'text' is required
                if not step.has_key('text'):
                    print ('ERROR: "text" step must have "text" attribute with string value.')
                    return
            elif step['action'] == 'survey':
                # 'prompt' is required
                if not step.has_key('prompt'):
                    print ('ERROR: "survey" step must have "prompt" attribute with string value.')
                    return
                # 'options' list is required
                if not step.has_key('options'):
                    print ('ERROR: "survey" step must have "options" attribute with an array of string values.')
                    return
            elif step['action'] == 'blackscreen':
                # duration and trigger_count are both optional, so nothing to validate
                pass
            elif step['action'] == 'game':
                # level json must be valid. Try loading levels
                if not step.has_key('levels'):
                    print ('ERROR: "game" action must have levels attribute pointing to ' +
                           'levels list json file.')
                    return

                step['levellist'] = self.load_levels(step)
            elif step['action'] == 'game-adaptive':
                if not step.has_key('level_templates'):
                    print ('ERROR: "game" action must have level_templates attribute ' +
                        'with a list of level options or a string filename for a level ' +
                        'options json file, .')
                    return
                step['level_templates_list'] = self.load_level_templates(step)

                # float options
                if step.has_key('start_level'):
                    step['start_level'] = float(step['start_level'])
                if step.has_key('level_completion_increment'):
                    step['level_completion_increment'] = float(step['level_completion_increment'])
                if step.has_key('level_death_decrement'):
                    step['level_death_decrement'] = float(step['level_death_decrement'])
            elif step['action'] == 'parallel_port_test':
                # nothing else to validate
                pass

        resources.music_volume = self.args.music_volume
        resources.effects_volume = self.args.effects_volume

        if pygame.mixer:
            pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)

        displayflags = pygame.DOUBLEBUF
        if args.display_mode == 'fullscreen':
            displayflags |= pygame.FULLSCREEN
        else:
            # windowed
            if not self.args.parallel_test_address:
                displayflags |= pygame.NOFRAME
            if self.args.window_x != None and self.args.window_y != None:
                os.environ['SDL_VIDEO_WINDOW_POS'] = \
                    "%d,%d" % (self.args.window_x, self.args.window_y)
        screensize = (self.args.display_width, self.args.display_height)
        virtualdisplay.set_screensize(screensize)

        pygame.init()
        
        if not pygame.mixer.get_init():
            print 'Warning, could not initialize mixer. Game will have no sound.'

        if self.args.list_modes:
            print 'Available full screen display modes:'
            for mode in pygame.display.list_modes(0, pygame.DOUBLEBUF | pygame.FULLSCREEN):
                print '--display-mode fullscreen --display-width', mode[0], '--display-height', mode[1]
            # exit
            return

        self.screen = pygame.display.set_mode(screensize, displayflags)
        pygame.display.set_caption('Asteroid Impact')
        pygame.mouse.set_visible(0)
        # capture mouse
        pygame.event.set_grab(True)

        pygame.display.flip()

        # Init sequence of steps:
        self.stepindex = 0
        self.init_step()
        
        self.skipgame = False

    def init_step(self):
        "setup for next game mode step"
        self.step_millis = 0
        self.step_trigger_count = 0
        self.step_max_trigger_count = 2**64
        self.step_max_millis = None
        step = self.gamesteps[self.stepindex]

        if step.has_key('duration') and step['duration'] != None:
            self.step_max_millis = int(1000 * step['duration'])

        if step.has_key('trigger_count') and step['trigger_count'] != None:
            self.step_max_trigger_count = int(step['trigger_count'])

        self.gamescreenstack = []
        if step['action'] == 'instructions':
            click_to_continue = True
            if step.has_key('duration') and step['duration'] != None:
                click_to_continue = False
            if step.has_key('trigger_count') and step['trigger_count'] != None:
                click_to_continue = False

            self.gamescreenstack.append(
                AsteroidImpactInstructionsScreen(
                    self.screen,
                    self.gamescreenstack,
                    click_to_continue=click_to_continue))
        elif step['action'] == 'text':
            click_to_continue = True
            if step.has_key('duration') and step['duration'] != None:
                click_to_continue = False
            if step.has_key('trigger_count') and step['trigger_count'] != None:
                click_to_continue = False

            self.gamescreenstack.append(
                UserTextScreen(
                    self.screen,
                    self.gamescreenstack,
                    click_to_continue=click_to_continue,
                    text=step['text']))
        elif step['action'] == 'survey':
            self.gamescreenstack.append(
                SurveyQuestionScreen(
                    self.screen,
                    self.gamescreenstack,
                    prompt=step['prompt'],
                    survey_options=step['options']))
        elif step['action'] == 'blackscreen':
            self.gamescreenstack.append(BlackScreen(self.screen, self.gamescreenstack))
        elif step['action'] == 'game':
            self.gamescreenstack.append(
                AsteroidImpactGameplayScreen(
                    self.screen,
                    self.gamescreenstack,
                    step['levellist'],
                    step['reaction_prompts']))
        elif step['action'] == 'game-adaptive':
            kwargs = {}
            if step.has_key('start_level'):
                kwargs['start_level'] = step['start_level']
            if step.has_key('level_completion_increment'):
                kwargs['level_completion_increment'] = step['level_completion_increment']
            if step.has_key('level_death_decrement'):
                kwargs['level_death_decrement'] = step['level_death_decrement']

            self.gamescreenstack.append(
                AsteroidImpactInfiniteGameplayScreen(
                    self.screen,
                    self.gamescreenstack,
                    step['level_templates_list'],
                    step['reaction_prompts'],
                    **kwargs))
        elif step['action'] == 'parallel_port_test':
            self.gamescreenstack.append(
                ParallelPortTestScreen(
                    self.screen,
                    self.gamescreenstack,
                    port_address=step['parallel_test_address']))
        else:
            raise ValueError('Unknown step action "%s"'%step['action'])


    def load_levels(self, step):
        "Load level details for game step from inline JSON or file"
        if isinstance(step['levels'], list):
            levellist = step['levels']
            dir = ''
        else:
            levelsabspath = os.path.abspath(step['levels'])
            dir, levellistfile = os.path.split(levelsabspath)

            "load levels from list of levels in JSON file"
            # load level list
            with open(path.join(dir, levellistfile)) as f:
                levellist = json.load(f)['levels']

        # load all levels in list
        levels = []
        # todo: allow level list of levels, not just level files?
        for levelfile in levellist:
            with open(path.join(dir, levelfile)) as f:
                level = json.load(f)
                level['level_name'] = levelfile
                levels.append(level)

        # find max # asteroids
        for level in levels:
            self.max_asteroid_count = max(
                self.max_asteroid_count, len(level['asteroids']))
                
        return levels
    
    def load_level_templates(self, step):
        "Load level templates for game-adaptive step from inline JSON or file"
        if isinstance(step['level_templates'], list):
            levellist = step['level_templates']
            dir = ''
        else:
            levelsabspath = os.path.abspath(step['level_templates'])
            dir, levellistfile = os.path.split(levelsabspath)

            "load levels from list of levels in JSON file"
            # load level list
            with open(path.join(dir, levellistfile)) as f:
                levellist = json.load(f)['levels']

        # load all levels in list
        levels = []
        for levelentry in levellist:
            if isinstance(levelentry, str):
                with open(path.join(dir, levelentry)) as f:
                    level = json.load(f)
                    level['level_name'] = levelentry
                    levels.append(level)
            else:
                levels.append(levelentry)

        # foo
        for level in levels:
            self.max_asteroid_count = max(
                self.max_asteroid_count, level['asteroid_count'])

        return levels

    def gameloop(self):
        "run the game frame/tick loop"

        if self.skipgame:
            # exit
            return

        clock = pygame.time.Clock()

        if pygame.mixer and pygame.mixer.get_init():
            resources.load_music('through space.ogg')
            resources.unmute_music()
            pygame.mixer.music.play(-1)

        asteroidlogger = AsteroidLogger(self.args.log_filename, self.args.log_overwrite == 'true', self.max_asteroid_count)
        logrowdetails = {}

        self.total_millis = 0

        # cheesy 'framerate' display
        # mostly used to indicate if I'm getting 60fps or 30fps
        fps_display_enable = False
        import sprites
        fps_sprite = Target(diameter=8)
        fps_sprite.rect.top = 0
        fps_sprite_group = pygame.sprite.Group([fps_sprite])
        
        # trigger blink sprite
        trigger_blink_sprite = Target(diameter=32)
        trigger_blink_sprite.rect.top = 480-24
        trigger_blink_sprite.rect.left = 640-230
        
        if self.args.trigger_blink == 'true':
            trigger_blink_sprites = pygame.sprite.Group([trigger_blink_sprite])
        else:
            trigger_blink_sprites = pygame.sprite.Group([])

        if self.args.parallel_test_address:
            # try to parse parallel port address
            pport_debug_addr = int(self.args.parallel_test_address, 16)
            
            # ignore step list and just launch my new window
# hack todo: replace step list with just this step
            self.gamescreenstack = []
            self.gamescreenstack.append(
                ParallelPortTestScreen(
                    self.screen,
                    self.gamescreenstack,
                    port_address=pport_debug_addr))
        else:
            pport_debug_addr = None

        #Main Loop
        while 1:
            # more consistent, more cpu
            real_millis = clock.tick_busy_loop(60)
            trigger_received_this_tick = False
            # less repeatable, less cpu:
            #real_millis = clock.tick(60)

            if real_millis >= 25:
                # if we're not getting 60fps, then run update() extra times
                # find new frame durations that add-up to real_millis:
                frames = int(round(real_millis * .001 * 60))
                millis_list = [16] * frames
                millis_list[-1] = real_millis - 16 * (frames-1)
            else:
                millis_list = (real_millis,)

            for millis in millis_list:
                self.total_millis += millis
                self.step_millis += millis

                logrowdetails.clear()
                logrowdetails['subject_number'] = self.args.subject_number
                logrowdetails['subject_run'] = self.args.subject_run
                logrowdetails['step_number'] = self.stepindex + 1
                logrowdetails['total_millis'] = self.total_millis
                logrowdetails['step_number'] = self.stepindex + 1
                logrowdetails['step_millis'] = self.step_millis
                logrowdetails['top_screen'] = self.gamescreenstack[-1].name

                #Handle Input Events

                # update the topmost screen:
                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        return
                    elif (event.type == KEYDOWN
                          and event.key == K_q
                          and (event.mod & pygame.KMOD_META)):
                        print 'CMD+Q Pressed. Exiting'
                        return
                    elif (event.type == KEYDOWN 
                          and event.key == K_F4
                          and (event.mod & pygame.KMOD_ALT)):
                        print 'ALT+F4 Pressed. Exiting'
                        return
                    elif (event.type == KEYDOWN
                          and event.key == K_c
                          and (event.mod & pygame.KMOD_ALT) != 0):
                        # toggle cursor capture and visibility:
                        current_grab = pygame.event.get_grab()
                        new_grab = not current_grab
                        pygame.event.set_grab(new_grab)
                        pygame.mouse.set_visible(not new_grab)
                    elif (event.type == KEYDOWN
                          and event.key == K_n
                          and (event.mod & pygame.KMOD_CTRL)):
                        print 'CTRL+n pressed. Advancing to next step'
                        for screen in reversed(self.gamescreenstack):
                            screen.after_close()
                        self.gamescreenstack = []
                    else:
                        # check for keyboard trigger
                        if (self.trigger_enabled
                            and self.trigger_key != None 
                            and event.type == KEYDOWN 
                            and event.key == self.trigger_key):
                            self.step_trigger_count += 1
                            trigger_received_this_tick = True
                        pass
                        #print event

                # Check for serial trigger:
                if self.trigger_enabled and self.trigger_serialport != None:
                    serial_input = self.trigger_serialport.read()
                    if serial_input:
                        for c in serial_input:
                            if ord(c) == self.trigger_serialport_byte_value:
                                self.step_trigger_count += 1
                                trigger_received_this_tick = True
                        # debug print:
                        print ">", repr(serial_input)
                        sys.stdout.flush()
                
                logrowdetails['step_trigger_count'] = self.step_trigger_count
                    
                try:
                    if len(self.gamescreenstack) > 0:
                        # update frontmost screen
                        self.gamescreenstack[-1].update_frontmost(millis, logrowdetails, events, self.step_trigger_count)
                        # update all screens in stack front to back
                        for screen in reversed(self.gamescreenstack):
                            screen.update_always(millis, logrowdetails, events, self.step_trigger_count)
                except QuitGame as e:
                    print e
                    return

                # Check if max duration on this step has expired
                step = self.gamesteps[self.stepindex]
                if self.step_max_millis != None and self.step_max_millis < self.step_millis:
                    # end this step:
                    for screen in reversed(self.gamescreenstack):
                        screen.after_close()
                    self.gamescreenstack = []
                
                # Check if max trigger count on this step has expired
                if self.step_max_trigger_count != None and self.step_max_trigger_count <= self.step_trigger_count:
                    # end this step
                    for screen in reversed(self.gamescreenstack):
                        screen.after_close()
                    self.gamescreenstack = []

                if len(self.gamescreenstack) == 0:
                    self.stepindex += 1
                    if self.stepindex >= len(self.gamesteps):
                        # all steps completed
                        return
                    self.init_step()
                    # Switch to gameplay

                asteroidlogger.log(logrowdetails)


            # draw topmost opaque screen and everything above it
            topopaquescreenindex = -1
            for i in range(-1, -1-len(self.gamescreenstack), -1):
                topopaquescreenindex = i
                if self.gamescreenstack[i].opaque:
                    break

            for screenindex in range(topopaquescreenindex, 0, 1):
                self.gamescreenstack[screenindex].draw()

            # cheesy 'no text' FPS display
            fps_sprite.rect.left = real_millis
            fps_sprite.rect.top = 16 * (int(round(real_millis * .001 * 60))-1)
            if fps_display_enable:
                fps_sprite_group.draw(self.screen)
            
            if trigger_received_this_tick:
                trigger_blink_sprites.draw(self.screen)

            pygame.display.flip()

def main():
    "parse console arguments and start game"
    args = parser.parse_args()

    game_step_manager = GameModeManager(args)
    game_step_manager.gameloop()

if __name__ == '__main__':
    main()
