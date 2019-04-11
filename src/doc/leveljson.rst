*****************
Single Level JSON
*****************

This page describes the structure and meaning of the JSON file that specifies the details for a single level. Typically you wouldn't generate these files yourself, but instead use `makelevel.py` or make your own level generator by copying and modifying `standardlevels.py`

Game Coordinates
======================

The sizes, speeds, and positions in this file are specified in game coordinates, not pixels. This allows the screen resoloution to change but the game objects will still move and appear in the same way.

The game play area is 1280 units wide, 896 units tall.


Top level
====================

The single level JSON file's top level is a dictionary with the following 3 keys. The value for each is a list further described below.

 * `asteroids` List of asteroids in level to avoid.
 * `target_positions` List of positions for targets (crystals) for the player to pick up.
 * `powerup_list`` List of powerups that are available for the player to pick up.

``asteroids`` List
--------------------------

Each entry in the list of ``asteroids`` is a dictionary with the following keys:

``"diameter"``
    The diameter of the asteroid in game units. This must be an integer.
``"top"``
    The distance of the top of the asteroid from the top edge of the play area in game units. This sets the initial position when the asteroids start moving during the level countdown. This must be an integer.
``"left"``
     The distance of the left of the asteroid from the left edge of the play area in game units. This sets the initial position when the asteroids start moving during the level countdown. This must be an integer.
``"dx"``
    Distance along x moved per frame. This may be positive or negative or zero, but generated levels don't specify zero X or Y speeds. The sign of the speed is only used for the initial direction of the asteroid. This may be an integer or float.
``"dy"``
    Distance along y moved per frame. This may be positive or negative or zero, but generated levels don't specify zero X or Y speeds. The sign of the speed is only used for the initial direction of the asteroid. This may be an integer or float.

``top``, ``left``, ``dx``, ``dy`` specify the initial positions and direction of motion when the asteroids start moving during the level countdown. Both the position and the speeds change during gameplay, by moving, bouncing off edges, or being slowed down. The during-gameplay values are not saved back to the level.

``"target_positions"`` List
-----------------------------

The ``"target_positions"`` must be set to a list of 2-entry lists. The 2-entry lists represent ``[left, top]`` positions of the crystals to be picked up in the level. By default the crystals are 32 game units in diameter, and the level JSON currently has no way to specify otherwise.

``"powerup_list"`` List
------------------------

Powerups will spawn in order, starting with the first one in the list and looping back to the first after using up the last powerup. The next powerup spawns after the player picks up a powerup and its expires after its delay. None powerups are picked up instantly (and invisibly) so are used to introduce a delay after one powerup is used before the next is available. For example, to have a 3s delay between the player's shield ending and another becoming available, the list should have a shield, none with 3s delay, then another shield.

There must be at least one entry in this list. If you don't want the player to have a powerup in this level, put a ``"type":"none"`` powerup with a delay in the list instead.

The ``powerup_list`` is a list of objects with the keys listed below.

``"type"``
    Must be one of ``shield``, ``slow``, or ``none``
``"diameter"``
    Usually 32 game units for ``shield`` or ``slow``. Don't specify this on a ``"type":"none"`` powerup.
``"left"``
    The distance from the left edge of the powerup to the left edge of the game play area.
``"top"``
    The distance from the left edge of the powerup to the left edge of the game play area.
``"duration"``
    The number of seconds this powerup lasts, as a number. This is required for, and should only be specified on ``"type":"none"`` powerups.


Sample file
===================

::

    {
        "asteroids": [
            {
                "diameter": 160,
                "top": 578,
                "left": 722,
                "dx": -3,
                "dy": -4
            },
            {
                "diameter": 160,
                "top": 333,
                "left": 265,
                "dx": 11,
                "dy": -1
            },
            {
                "diameter": 160,
                "top": 231,
                "left": 43,
                "dx": -8,
                "dy": -13
            },
            {
                "diameter": 200,
                "top": 462,
                "left": 820,
                "dx": -9,
                "dy": 1
            },
            {
                "diameter": 170,
                "top": 167,
                "left": 886,
                "dx": -4,
                "dy": -4
            }
        ],
        "target_positions": [
            [
                1051,
                65
            ],
            [
                593,
                722
            ],
            [
                184,
                417
            ],
            [
                592,
                64
            ],
            [
                1154,
                58
            ],
            [
                473,
                561
            ],
            [
                685,
                82
            ],
            [
                1014,
                249
            ],
            [
                787,
                34
            ],
            [
                351,
                286
            ],
            [
                56,
                386
            ],
            [
                554,
                589
            ]
        ],
        "powerup_list": [
            {
                "diameter": 32,
                "top": 668,
                "type": "shield",
                "left": 838
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 747,
                "type": "shield",
                "left": 926
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 479,
                "type": "shield",
                "left": 502
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 72,
                "type": "shield",
                "left": 236
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 132,
                "type": "shield",
                "left": 96
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 691,
                "type": "shield",
                "left": 374
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 29,
                "type": "shield",
                "left": 56
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 704,
                "type": "shield",
                "left": 391
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 37,
                "type": "shield",
                "left": 427
            },
            {
                "duration": 0.5,
                "type": "none"
            },
            {
                "diameter": 32,
                "top": 104,
                "type": "shield",
                "left": 394
            },
            {
                "duration": 0.5,
                "type": "none"
            }
        ]
    }

