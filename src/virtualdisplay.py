# Asteroid Impact (c) by Nick Winters
# 
# Asteroid Impact is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>. 
"""
Virtual display transformation back and forth from screen coordinates and rectangles
to game coordinates and rectangles.

This is needed to allow the game to run at multiple resolutions, but have game objects
move the same way. The game coordinate system is scaled up and down, and translated to
fit the available screen space.
"""

from __future__ import absolute_import, division
from pygame import Rect

# virtual game area is always the same "resolution" and aspect ratio
GAME_AREA = Rect(0, 0, 640*2, 480*2)
# virtual game play area (room that asteroids and player bounce around in)
GAME_PLAY_AREA = Rect(0,0, GAME_AREA.width, GAME_AREA.height - 64)

# screen area and transform may vary depending on screen window size
# so these values are changed in set_screensize() below
screenarea = GAME_AREA.copy()
screenplayarea = screenarea.copy()

# screen_from_game:
s_f_g_w = 1.0
s_f_g_h = 1.0
s_f_g_x = 0.0
s_f_g_y = 0.0

# game_from_screen
g_f_s_w = 1.0
g_f_s_h = 1.0
g_f_s_x = 0.0
g_f_s_y = 0.0

def set_screensize(screensize):
    """
    Set the physical screen size in pixels.

    Calculates the transformations to and from game space, using an aspect-preserving
    scale.
    """
    global screenarea, screenplayarea
    global s_f_g_w, s_f_g_h, s_f_g_x, s_f_g_y
    global g_f_s_w, g_f_s_h, g_f_s_x, g_f_s_y

    # find screenarea rect
    # the rect in screen space that the game will take up
    # by doing an aspect preserve scale, and centering in the middle of the screen
    if screensize[0] / screensize[1] > GAME_AREA.width / GAME_AREA.height:
        # game uses full height of screen
        screenarea = Rect(0, 0, screensize[1]*GAME_AREA.width/GAME_AREA.height, screensize[1])
        screenarea.centerx = screensize[0]/2
    else:
        # game uses full width of screen
        screenarea = Rect(0, 0, screensize[0], screensize[0]*GAME_AREA.height/GAME_AREA.width)
        screenarea.centery = screensize[1]/2

    # screen_from_game:
    s_f_g_w = screenarea.width / GAME_AREA.width
    s_f_g_h = screenarea.height / GAME_AREA.height
    s_f_g_x = screenarea.x - GAME_AREA.x * s_f_g_w
    s_f_g_y = screenarea.y - GAME_AREA.y * s_f_g_h

    # game_from_screen
    g_f_s_w = GAME_AREA.width / screenarea.width
    g_f_s_h = GAME_AREA.height / screenarea.height
    g_f_s_x = GAME_AREA.x - screenarea.x * g_f_s_w
    g_f_s_y = GAME_AREA.y - screenarea.y * g_f_s_h
    
    screenplayarea = screenrect_from_gamerect(GAME_PLAY_AREA)


def screenrect_from_gamerect(gamerect):
    """Returns the corresponding (transformed) screen space rectangle for the supplied
    rectangle in game-space"""
    return Rect(
        s_f_g_x + gamerect.x * s_f_g_w,
        s_f_g_y + gamerect.y * s_f_g_h,
        gamerect.width * s_f_g_w,
        gamerect.height * s_f_g_h)

def screenpoint_from_gamepoint(gamepoint):
    """Returns the corresponding (transformed) screen space point for the supplied
    point in game-space"""
    return (
        s_f_g_x + gamepoint[0] * s_f_g_w,
        s_f_g_y + gamepoint[1] * s_f_g_h)

def gamerect_from_screenrect(screenrect):
    """Returns the corresponding (transformed) game space rectangle for the supplied
    rectangle in screen-space"""
    return Rect(
        g_f_s_x + screenrect.x * g_f_s_w,
        g_f_s_y + screenrect.y * g_f_s_h,
        screenrect.width * g_f_s_w,
        screenrect.height * g_f_s_h)

def gamepoint_from_screenpoint(point):
    """Returns the corresponding (transformed) game space point for the supplied
    point in screen-space"""
    return (
        g_f_s_x + point[0] * g_f_s_w,
        g_f_s_y + point[1] * g_f_s_h)

