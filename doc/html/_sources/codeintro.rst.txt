*********************************
Asteroid Impact Code Introduction
*********************************

The game logic is divided into screens which each implement the behavior for a given step or portion of a step. For example, the survey step is one screen, gameplay is another, and so is just the "game over" text that appears on top of gameplay.

Screen Stack
------------------

The game screens are a stack of windows on top of each other like modal dialog windows. Only the topmost one is in charge of deciding what happens in this game tick.

These are a stack of windows to make the transition between menus easier. For example a game might have a main menu, and a settings screen, gameplay, and a pause screen. The main screen would open the gameplay on top of the main screen, so when gameplay ends you'd end up back at the menu. This makes it easier in the future to add level select and return to them when leaving the game. The same is true for having a pause screen on top of gameplay or a settings screen accessible from both the pause menu and main menu.

The process of a typical frame
------------------------------------

This starts in the main game loop is in [GameModeManager.gameloop()] in ``game.py``

 1. we wait 1/60th of a second (clock.tick_busy_loop(60)
 2. Set up known frame log row details
 3. Check for global input events (quitting the game, serial or parallel input triggers)
 4. Update the topmost game screen. When the game is running this calls AsteroidImpactGameplayScreen.update()

    1. AsteroidImpactGameplayScreen.update() works as follows:
    2. Handle gameplay input events.
    3. Update the moving sprites for the current frame. Every sprite has an update() method which is called here.
    4. If we aren't at the level countdown, check for collisions with powerup, next target (next crystal), and all asteroids. These may advance the player to the next levels, enable a powerup (by calling .activate() on the sprite), or notice the player has died.

 5. Then, back in GameModeManager.gameloop() we check for if we've exceeded the duration for this step, for example if the gameplay was limited to 60 seconds and we've exceeded that time. If so we wipe out the screen stack and build it again for the next step.
 6. Save the details to the log file
 7. Draw the currently visible screens.

Game coordinates
--------------------------

To allow the game to scale up and down, the gameplay happens in its own coordinate space which is scaled up or down for the current screen or window. This allows the screen resoloution to change but the game objects will still move and appear in the same way.

The game play area is 1280 units wide, 896 units tall. The center of the window or screen would be at (640,480) and the top left is (0,0).

Sprites
-------------
Everything drawn to the screen exists as a sprite object in sprites.py, including text. The sprites contain logic for how to move on each frame and when to play their sound effects.

The code is split along a handful of files described below. Before diving in, please read the overview of how a single frame works to get an idea where the logic for each lives.

Source Files and Directories
------------------------------

 * ``doc/`` Documentation such as this file.
 * ``data/`` Game assets such as images, sounds and music.
 * ``levels/`` Standard game level JSON files.
 * ``raw_data/`` Source files for some game assets. Images with layers, or higher bitrate audio files live here, and are flattened or resampled to the ones in the ``data/`` folder. This folder is not required to run the game and is not included with the standalone exe build.
 * ``game.py`` Entry point for game, command-line options, game loop.
 * ``logger.py`` Saves each row to CSV file.
 * ``makelevel.py`` Used to create a new level from command-line.
 * ``makestandardlevels.py`` Creates the standard levels in the ``levels/`` folder.
 * ``resources.py`` Game asset (image, sound, music) loading and caching.
 * ``screens.py`` Game screens such as instructions, black screen, and gameplay. Most of the game logic happens in the gameplay screen.
 * ``sprites.py`` Sprite logic for movement and behavior of asteroids and powerups.
 * ``virtualdisplay.py`` Converts from game coordinates to screen coordinates and back to allow the game to run at multiple resolutions.
 * ``pyinstaller-build-windows.bat`` Using pyinstaller, create an exe of the game that doesn't require a python installation.

