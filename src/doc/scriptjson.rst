******************
 Game Script JSON 
******************

AsteroidImpact will optionally run a sequence of modes specified in script.json. This can be used to advance the player between multiple lists of levels, with blank screens inbetween. Advancing to the next step happens after a specified duration, or for the instructions screen when the user clicks with the mouse.

Sample: ::

    {
      "output_trigger_settings": {
        "mode": "none",

        "serial_trigger_strings_by_event": {
          "step_begin": "1",
          "game_level_begin": "2",
          "game_level_complete": "3",
          "game_death": "4",
          "game_shield_activate": "5",
          "game_slow_activate": "6",
          "game_crystal_collected": "7",
          "adaptive_difficulty_increase": "8",
          "adaptive_difficulty_decrease": "9"
        },
        "serial_options": {
          "port": "COM6",
          "baudrate": 19200
        },

        "parallel_trigger_hex_values_by_event": {
          "step_begin": "0x01",
          "game_level_begin": "0x02",
          "game_level_complete": "0x04",
          "game_death": "0x08",
          "game_shield_activate": "0x10",
          "game_slow_activate": "0x20",
          "game_crystal_collected": "0x40",
          "adaptive_difficulty_increase": "0x80",
          "adaptive_difficulty_decrease": "0xFF"
        },
        "parallel_options": {
          "port_address_hex": "BF00",
          "common_data_value_hex": "0x10",
          "trigger_frames": 3
        }
      },
      "steps": [
        {
          "action": "instructions",
          "duration": 10.0
        },
        {
          "action": "game",
          "levels": "levels/standardlevels.json",
          "duration": 20.0,
          "reaction_prompts": [
            {
              "diameter": 80,
              "position_list": [
                [ 200, 200 ],
                [ 200, 300 ],
                [ 200, 400 ],
                [ 200, 500 ],
                [ 200, 600 ]
              ],
              "image": "triangle.png",
              "sound": "tone440.wav",
              "showtimes_millis": [ 1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000, 37000, 39000, 41000, 43000, 45000, 47000, 49000, 51000, 53000, 55000, 57000, 59000, 61000, 63000, 65000, 67000, 69000, 71000, 73000, 75000, 77000, 79000, 81000, 83000, 85000, 87000, 89000, 91000, 93000, 95000, 97000, 99000, 101000, 103000, 105000, 107000, 109000, 111000, 113000, 115000, 117000, 119000, 121000, 123000, 125000, 127000, 129000, 131000, 133000, 135000, 137000, 139000, 141000, 143000, 145000, 147000, 149000, 151000, 153000, 155000, 157000, 159000, 161000, 163000, 165000, 167000, 169000, 171000, 173000, 175000, 177000, 179000, 181000, 183000, 185000, 187000, 189000, 191000, 193000, 195000, 197000, 199000 ],
              "showtimes_trigger_counts": [],
              "input_key": "K_1",
              "timeout_millis": 1500,
              "stay_visible": false
            },
            {
              "diameter": 80,
              "position_list": [
                [ 300, 200 ]
              ],
              "image": "circle.png",
              "sound": "tone659.wav",
              "showtimes_millis": [ 1500, 3500, 5500, 7500, 9500, 11500, 13500, 15500, 17500, 19500, 21500, 23500, 25500, 27500, 29500, 31500, 33500, 35500, 37500, 39500, 41500, 43500, 45500, 47500, 49500, 51500, 53500, 55500, 57500, 59500, 61500, 63500, 65500, 67500, 69500, 71500, 73500, 75500, 77500, 79500, 81500, 83500, 85500, 87500, 89500, 91500, 93500, 95500, 97500, 99500, 101500, 103500, 105500, 107500, 109500, 111500, 113500, 115500, 117500, 119500, 121500, 123500, 125500, 127500, 129500, 131500, 133500, 135500, 137500, 139500, 141500, 143500, 145500, 147500, 149500, 151500, 153500, 155500, 157500, 159500, 161500, 163500, 165500, 167500, 169500, 171500, 173500, 175500, 177500, 179500, 181500, 183500, 185500, 187500, 189500, 191500, 193500, 195500, 197500, 199500 ],
              "showtimes_trigger_counts": [],
              "input_key": "K_2",
              "timeout_millis": 1500,
              "stay_visible": false
            },
            {
              "diameter": 80,
              "position_list": [
                [ 400, 200 ]
              ],
              "image": "square.png",
              "sound": "tone146.wav",
              "showtimes_millis": [],
              "showtimes_trigger_counts": [ 1, 2, 3, 4, 5, 6 ],
              "input_key": "K_MOUSE1",
              "timeout_millis": "never",
              "stay_visible": false
            }
          ]
        },
        {
          "action": "text",
          "text": "Custom instructions can appear here. They can be split into paragraphs by escaping newlines.\n\nThis is a second paragraph.\n\nThe next step after this one is a 5 second black screen.",
          "duration": 20.0
        },
        {
          "action": "blackscreen",
          "duration": 5.0
        },
        {
          "action": "survey",
          "prompt": "Bacon ipsum dolor amet tail ribeye cow prosciutto flank. Short ribs sausage leberkas boudin biltong jerky swine spare ribs flank salami kevin short loin pork chop. Meatloaf drumstick spare ribs ball tip venison meatball. Picanha biltong t-bone fatback flank ribeye. Pork shoulder meatloaf beef, bresaola meatball ground round filet mignon. Tri-tip swine pork belly turkey, prosciutto filet mignon pork loin bresaola kielbasa pig biltong pork frankfurter. Tri-tip ham boudin biltong pig meatloaf pork belly pork tail shank t-bone shoulder pastrami.",
          "options": [ "one", "two", "three", "four", "five" ],
          "duration": 20.5
        },
        {
          "action": "game",
          "levels": "levels/hardlevels.json",
          "duration": 20.0
        },
        {
          "duration": 10.0,
          "action": "game-adaptive",
          "start_level": 0.5,
          "level_completion_increment": 0.3,
          "level_death_decrement": 0.4,
          "continuous_asteroids_on_same_level": false,
          "show_advance_countdown": false,
          "level_templates": [
            {
              "asteroid_count": 1,
              "asteroid_speeds": "slow",
              "powerup_count": 0,
              "target_count": 3
            },
            {
              "asteroid_count": 3,
              "asteroid_sizes": "varied",
              "asteroid_speeds": "medium",
              "powerup_count": 10,
              "powerup_delay": 0.5,
              "powerup_types": [
                "slow"
              ],
              "target_count": 3
            },
            {
              "asteroid_count": 8,
              "asteroid_sizes": "varied",
              "asteroid_speeds": "medium",
              "powerup_count": 10,
              "powerup_delay": 2.0,
              "powerup_types": [
                "slow",
                "shield"
              ],
              "target_count": 3
            },
            {
              "asteroid_count": 5,
              "asteroid_speeds": "extreme",
              "powerup_count": 10,
              "powerup_delay": 0.5,
              "powerup_types": [
                "shield"
              ],
              "target_count": 3
            }
          ]
        },
        {
          "action": "blackscreen",
          "duration": 5.0
        }
      ]
    }

Steps List
==========

Previous versions specified only the steps list in JSON. This continues to work, but you will not be able to use the trigger advance options.

Such a JSON file would look like this: ::

    [
        {
            "action": "instructions",
            "duration": 10.0
        },
        {
            "action": "game",
            "levels": "levels/standardlevels.json",
            "duration": 20.0
        },
        {
            "action": "text",
            "text": "Custom instructions can appear here. They can be split into paragraphs by escaping newlines.\n\nThis is a second paragraph.\n\nThe next step after this one is a 5 second black screen.",
            "duration": 20.0
        },
        {
            "action": "blackscreen",
            "duration": 5.0
        },
        {
            "action": "game",
            "levels": "levels/hardlevels.json",
            "duration": 20.0
        }
    ]

Trigger Advance Options
=======================

Rather than advancing steps after a duration, they can be advanced after receiving a number of "trigger" pulses. The pulses can come as key presses or as characters over a serial port. The step advances to the next step after receiving the number of pulses specified for the trigger_count attribute.

You can visualize trigger pulses on screen by using the ``--trigger-blink true`` command-line option.

Sample trigger-driven JSON: ::

    {
      "trigger_settings": {
        "mode": "keyboard",

        "serial_options": {
          "port": "COM5",
          "baudrate": 19200,
          "trigger_byte_value": 53
        },

        "keyboard_options": {
          "trigger_key": "K_5"
        },

        "parallel_options": {
          "port_address_hex": "BF00",
          "common_status_value_hex": "0x00",
          "trigger_status_value_hex": "0x08"
        }
      },
      "output_trigger_settings": {
        "mode": "none",

        "serial_trigger_strings_by_event": {
          "step_begin": "1",
          "game_level_begin": "2",
          "game_level_complete": "3",
          "game_death": "4",
          "game_shield_activate": "5",
          "game_slow_activate": "6",
          "game_crystal_collected": "7",
          "adaptive_difficulty_increase": "8",
          "adaptive_difficulty_decrease": "9"
        },
        "serial_options": {
          "port": "COM6",
          "baudrate": 19200
        },

        "parallel_trigger_hex_values_by_event": {
          "step_begin": "0x01",
          "game_level_begin": "0x02",
          "game_level_complete": "0x04",
          "game_death": "0x08",
          "game_shield_activate": "0x10",
          "game_slow_activate": "0x20",
          "game_crystal_collected": "0x40",
          "adaptive_difficulty_increase": "0x80",
          "adaptive_difficulty_decrease": "0xFF"
        },
        "parallel_options": {
          "port_address_hex": "BF00",
          "common_data_value_hex": "0x10",
          "trigger_frames": 3
        }
      },
      "steps": [
        {
          "action": "instructions",
          "trigger_count": 10
        },
        {
          "action": "game",
          "levels": "levels/standardlevels.json",
          "trigger_count": 10,
          "reaction_prompts": [
            {
              "diameter": 80,
              "position_list": [
                [ 200, 200 ],
                [ 200, 300 ],
                [ 200, 400 ],
                [ 200, 500 ],
                [ 200, 600 ]
              ],
              "image": "triangle.png",
              "sound": "tone440.wav",
              "showtimes_millis": [ 1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000, 37000, 39000, 41000, 43000, 45000, 47000, 49000, 51000, 53000, 55000, 57000, 59000, 61000, 63000, 65000, 67000, 69000, 71000, 73000, 75000, 77000, 79000, 81000, 83000, 85000, 87000, 89000, 91000, 93000, 95000, 97000, 99000, 101000, 103000, 105000, 107000, 109000, 111000, 113000, 115000, 117000, 119000, 121000, 123000, 125000, 127000, 129000, 131000, 133000, 135000, 137000, 139000, 141000, 143000, 145000, 147000, 149000, 151000, 153000, 155000, 157000, 159000, 161000, 163000, 165000, 167000, 169000, 171000, 173000, 175000, 177000, 179000, 181000, 183000, 185000, 187000, 189000, 191000, 193000, 195000, 197000, 199000 ],
              "showtimes_trigger_counts": [],
              "input_key": "K_1",
              "timeout_millis": 1500,
              "stay_visible": false
            },
            {
              "diameter": 80,
              "position_list": [
                [ 300, 200 ]
              ],
              "image": "circle.png",
              "sound": "tone659.wav",
              "showtimes_millis": [ 1500, 3500, 5500, 7500, 9500, 11500, 13500, 15500, 17500, 19500, 21500, 23500, 25500, 27500, 29500, 31500, 33500, 35500, 37500, 39500, 41500, 43500, 45500, 47500, 49500, 51500, 53500, 55500, 57500, 59500, 61500, 63500, 65500, 67500, 69500, 71500, 73500, 75500, 77500, 79500, 81500, 83500, 85500, 87500, 89500, 91500, 93500, 95500, 97500, 99500, 101500, 103500, 105500, 107500, 109500, 111500, 113500, 115500, 117500, 119500, 121500, 123500, 125500, 127500, 129500, 131500, 133500, 135500, 137500, 139500, 141500, 143500, 145500, 147500, 149500, 151500, 153500, 155500, 157500, 159500, 161500, 163500, 165500, 167500, 169500, 171500, 173500, 175500, 177500, 179500, 181500, 183500, 185500, 187500, 189500, 191500, 193500, 195500, 197500, 199500 ],
              "showtimes_trigger_counts": [],
              "input_key": "K_2",
              "timeout_millis": 1500,
              "stay_visible": false
            },
            {
              "diameter": 80,
              "position_list": [
                [ 400, 200 ]
              ],
              "image": "square.png",
              "sound": "tone146.wav",
              "showtimes_millis": [],
              "showtimes_trigger_counts": [ 1, 2, 3, 4, 5, 6 ],
              "input_key": "K_MOUSE1",
              "timeout_millis": "never",
              "stay_visible": false
            }
          ]
        },
        {
          "action": "text",
          "text": "Custom instructions can appear here. They can be split into paragraphs by escaping newlines.\n\nThis is a second paragraph.\n\nThe next step after this one is a 5 second black screen.",
          "trigger_count": 10
        },
        {
          "action": "blackscreen",
          "trigger_count": 5
        },
        {
          "action": "survey",
          "prompt": "Bacon ipsum dolor amet tail ribeye cow prosciutto flank. Short ribs sausage leberkas boudin biltong jerky swine spare ribs flank salami kevin short loin pork chop. Meatloaf drumstick spare ribs ball tip venison meatball. Picanha biltong t-bone fatback flank ribeye. Pork shoulder meatloaf beef, bresaola meatball ground round filet mignon. Tri-tip swine pork belly turkey, prosciutto filet mignon pork loin bresaola kielbasa pig biltong pork frankfurter. Tri-tip ham boudin biltong pig meatloaf pork belly pork tail shank t-bone shoulder pastrami.",
          "options": [ "one", "two", "three", "four", "five" ],
          "trigger_count": 25
        },
        {
          "action": "game",
          "levels": "levels/hardlevels.json",
          "trigger_count": 20
        },
        {
          "trigger_count": 10,
          "action": "game-adaptive",
          "start_level": 0.5,
          "level_completion_increment": 0.3,
          "level_death_decrement": 0.4,
          "continuous_asteroids_on_same_level": false,
          "show_advance_countdown": false,
          "level_templates": [
            {
              "asteroid_count": 1,
              "asteroid_speeds": "slow",
              "powerup_count": 0,
              "target_count": 3
            },
            {
              "asteroid_count": 3,
              "asteroid_sizes": "varied",
              "asteroid_speeds": "medium",
              "powerup_count": 10,
              "powerup_delay": 0.5,
              "powerup_types": [
                "slow"
              ],
              "target_count": 3
            },
            {
              "asteroid_count": 8,
              "asteroid_sizes": "varied",
              "asteroid_speeds": "medium",
              "powerup_count": 10,
              "powerup_delay": 2.0,
              "powerup_types": [
                "slow",
                "shield"
              ],
              "target_count": 3
            },
            {
              "asteroid_count": 5,
              "asteroid_speeds": "extreme",
              "powerup_count": 10,
              "powerup_delay": 0.5,
              "powerup_types": [
                "shield"
              ],
              "target_count": 3
            }
          ]
        },
        {
          "action": "blackscreen",
          "trigger_count": 10
        }
      ]
    }


The serial trigger mode opens a serial port on the computer and when a byte is received with the value matching ``trigger_byte_value`` increases the trigger count. The ``port`` setting is the serial port, typically ``COM1`` through ``COM16`` on Windows, or ``/dev/cu.usbmodem1234`` or similar on OSX. If you have python and pyserial installed, you can list serial ports from the command-line by running ``python -m serial.tools.list_ports`` which will print out serial ports on your computer. You can also specify the ``baudrate`` for serial connections. The ``trigger_byte_value`` of 53 is the ASCII code for the character "5".



Output Trigger Settings
=======================

The game can be configured to output signals over a serial port or parallel port on certain game events.

For serial output triggers, ``serial_trigger_strings_by_event`` is a lookup from game event to the string to send over serial. Configure this dictionary to contain only the events you wish to be notified about.

For parallel output triggers, ``parallel_trigger_hex_values_by_event`` is a lookup from game event to the value to change the parallel port data byte to for ``trigger_frames`` frames. One frame is about 1/60 second.

See :doc:``parallelport`` for information about parallel ports.

The full list of available game events to send an ouput trigger on are listed in the sample below.

Sample ::

    "output_trigger_settings": {
      "mode": "serial",

      "serial_trigger_strings_by_event": {
        "step_begin": "1",
        "game_level_begin": "2",
        "game_level_complete": "3",
        "game_death": "4",
        "game_shield_activate": "5",
        "game_slow_activate": "6",
        "game_crystal_collected": "7",
        "adaptive_difficulty_increase": "8",
        "adaptive_difficulty_decrease": "9"
      },
      "serial_options": {
        "port": "COM6",
        "baudrate": 19200
      },

      "parallel_trigger_hex_values_by_event": {
        "step_begin": "0x01",
        "game_level_begin": "0x02",
        "game_level_complete": "0x04",
        "game_death": "0x08",
        "game_shield_activate": "0x10",
        "game_slow_activate": "0x20",
        "game_crystal_collected": "0x40",
        "adaptive_difficulty_increase": "0x80",
        "adaptive_difficulty_decrease": "0xFF"
      },
      "parallel_options": {
        "port_address_hex": "BF00",
        "common_data_value_hex": "0x10",
        "trigger_frames": 3
      }
    },


Common Step Attributes
======================

Each step has the following attributes:

``"action"``
    The name of the action. Should be "instructions", "game", "text" or "blackscreen"
``"duration"``
    The duration in seconds (such as 12.5) after which to automatically advance to the next step. This can be null for some actions, see below.


Available step actions
=======================

``game``
--------

A null ``duration`` for the game step will prevent the player from advancing to the next step.

The ``levels`` value is required. It must point to a levels list json file. 

``instructions``
----------------

The ``instructions`` step displays instructions on how to play the game and each sprite the player will interact with.

A null ``duration`` for the instructions step will show a "Click to continue" message and allow the player to advance to the next step by clicking with their mouse. If a duration is specified the player will have to wait for that time to complete to move on to the next step.

``text``
----------------

The ``text`` step will display text specified in the ``text`` attribute on the screen for the specified duration with no available interaction to the player. The ``duration`` must be specified.

The text will be wrapped to fit on screen, but you can include newlines in the string and they will be included on string. Newlines in JSON must be escaped like ``\n``.

For example, here is text step with two lines of text with a blank line in between using two newline characters. ::

        {
            "action": "text",
            "text": "First Line\n\nSecond Line",
            "duration": 20.0
        },


``blackscreen``
----------------

The ``blackscreen`` step will display a black screen with no available interaction to the player. The ``duration`` must be specified.

``game-adaptive``
-----------------

The ``game-adaptive`` step will seamlessly transition between generated levels, advancing further in the level list as the player completes levels, and going backwards down the list as they fail. The intention is to tune the levels and how far back the list the player is put so that the player gets into a comfortable amount of difficulty and stays around there. 

A null ``duration`` for the game step will prevent the player from advancing to the next step.

The ``start_level`` is a float value that specifies the initial value used to choose the current level. ``0.0`` would start at the first level and ``1.0`` would start at the second level. The floor (integer part) of player's level score is used to index into the level options list.

``level_completion_increment`` is a float value for the amount the level score is incremented when the player completes a level. This can be under ``1.0`` which would usually mean that the player would have to complete another level with the same options before advancing to the next level in the list.

``level_death_decrement`` is a float value for the amount the level score is reduced when the player dies. This is distinct from the ``level_completion_increment`` so that the steady state reached when the player is near their effective difficulty can be tuned. The value should be a positive or zero.

``continuous_asteroids_on_same_level`` of ``true`` will keep the asteroids moving in their existing size and pattern when a player dying or completing a level does not advance all the way to a different level in the list. ``false`` is the default.

``show_advance_countdown`` of ``true`` will show the same countdown that happens when the player starts a level, but every time the difficulty increases. This defaults to ``false``.

The ``levels`` value is required. It must be a list of level parameters (which are different than for the ``game`` mode) or a string filename for a json file that contains a list of level parameters. 


game-adaptive levels list
=========================

The levels list is a list of objects with the following options:

+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| Option                                            | Values                                                 | Default        | Description                                                                                                  |
+===================================================+========================================================+================+==============================================================================================================+
| ``target_count``                                  | integer                                                | 5              | Number of crystals to pick up.                                                                               |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``asteroid_count``                                | integer                                                | 5              | Number of asteroids to avoid.                                                                                |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``asteroid_sizes``                                | one of the strings {"small","medium","large","varied"} | "large"        | Approximate size of asteroids.                                                                               |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``asteroid_speeds``                               | one of the strings {"slow","medium","fast","extreme"}  | "slow"         | Approximate speed of asteroids.                                                                              |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``powerup_count``                                 | integer                                                | 5              | Number of distinct power-ups to create for the player to pick up.                                            |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``powerup_initial_delay``                         | float                                                  | 0.0            | Delay in seconds before first powerup is available.                                                          |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``powerup_delay``                                 | float                                                  | 1.0            | Delay in seconds after powerup is used before next one becomes available.                                    |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``powerup_types``                                 | one of the strings {"shield","slow","all","none"}      | "all"          | Types of powerups that are in level.                                                                         |
+---------------------------------------------------+--------------------------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+

``survey``
----------------

The ``survey`` step will display a configurable prompt and list of options for the player. The player may click on one of the options to select it. If the player then clicks on a different option, the first is deselected.

If there is no ``duration`` or ``trigger_count`` attribute, the step will show a "Next" button to advance to the next step. The "Next" button does not become active to a until one of the survey options are selected.

Long text on the ``prompt`` option is fine. It will wrap to multiple lines.

Sample Survey Step with 20s duration and no Next button::

    {
      "action": "survey",
      "prompt": "Which of these is a better number?",
      "options": [ "one", "two", "three", "four", "five" ],
      "duration": 20.0
    },

Sample Survey Step with 5 pulse duration and no Next button::

    {
      "action": "survey",
      "prompt": "Which of these is a better number?",
      "options": [ "one", "two", "three", "four", "five" ],
      "trigger_count": 5
    },

Sample Survey Step with no duration a Next button::

    {
      "action": "survey",
      "prompt": "Which of these is a better number?",
      "options": [ "one", "two", "three", "four", "five" ]
    },



Reaction Prompt Elements
=========================

During the ``game`` and ``game-adaptive`` steps you can also configure reaction-time prompts to appear.

Sample game step with reaction prompts::

    {
      "action": "game",
      "levels": "levels/standardlevels.json",
      "trigger_count": 10,
      "reaction_prompts": [
        {
          "diameter": 80,
          "position_list": [
            [ 200, 200 ],
            [ 200, 300 ],
            [ 200, 400 ],
            [ 200, 500 ],
            [ 200, 600 ]
          ],
          "image": "triangle.png",
          "sound": "tone440.wav",
          "showtimes_millis": [ 1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000, 37000, 39000, 41000, 43000, 45000, 47000, 49000, 51000, 53000, 55000, 57000, 59000, 61000, 63000, 65000, 67000, 69000, 71000, 73000, 75000, 77000, 79000, 81000, 83000, 85000, 87000, 89000, 91000, 93000, 95000, 97000, 99000, 101000, 103000, 105000, 107000, 109000, 111000, 113000, 115000, 117000, 119000, 121000, 123000, 125000, 127000, 129000, 131000, 133000, 135000, 137000, 139000, 141000, 143000, 145000, 147000, 149000, 151000, 153000, 155000, 157000, 159000, 161000, 163000, 165000, 167000, 169000, 171000, 173000, 175000, 177000, 179000, 181000, 183000, 185000, 187000, 189000, 191000, 193000, 195000, 197000, 199000 ],
          "showtimes_trigger_counts": [],
          "input_key": "K_1",
          "timeout_millis": 1500,
          "stay_visible": false
        },
        {
          "diameter": 80,
          "position_list": [
            [ 300, 200 ]
          ],
          "image": "circle.png",
          "sound": "tone659.wav",
          "showtimes_millis": [ 1500, 3500, 5500, 7500, 9500, 11500, 13500, 15500, 17500, 19500, 21500, 23500, 25500, 27500, 29500, 31500, 33500, 35500, 37500, 39500, 41500, 43500, 45500, 47500, 49500, 51500, 53500, 55500, 57500, 59500, 61500, 63500, 65500, 67500, 69500, 71500, 73500, 75500, 77500, 79500, 81500, 83500, 85500, 87500, 89500, 91500, 93500, 95500, 97500, 99500, 101500, 103500, 105500, 107500, 109500, 111500, 113500, 115500, 117500, 119500, 121500, 123500, 125500, 127500, 129500, 131500, 133500, 135500, 137500, 139500, 141500, 143500, 145500, 147500, 149500, 151500, 153500, 155500, 157500, 159500, 161500, 163500, 165500, 167500, 169500, 171500, 173500, 175500, 177500, 179500, 181500, 183500, 185500, 187500, 189500, 191500, 193500, 195500, 197500, 199500 ],
          "showtimes_trigger_counts": [],
          "input_key": "K_2",
          "timeout_millis": 1500,
          "stay_visible": false
        },
        {
          "diameter": 80,
          "position_list": [
            [ 400, 200 ]
          ],
          "image": "square.png",
          "sound": "tone146.wav",
          "showtimes_millis": [],
          "showtimes_trigger_counts": [ 1, 2, 3, 4, 5, 6 ],
          "input_key": "K_MOUSE1",
          "timeout_millis": "never",
          "stay_visible": false
        }
      ]
    },

``"reaction_prompts"`` holds a list of entries. Each one has the following attributes:

``"diameter"``
    The game-unit width and height of the icon on screen.
``"position_list"``
   A list of 2-element positions. Each 2-element list is the [left, top] coordinate of the position of the image on screen in game coordinates. The first appearance is at the first entry in the list, second at the second entry and so-on, looping back to the first after the last.
``"image"``
    ``"none"`` or the filename of an image in the data directory. I've created ``"trinagle.png"``, ``"circle.png"`` and ``"square.png"`` but you may add your own transparent PNG images to the data directory and use them. Use "none" to create audio-only reaction prompts.
``"sound"``
    The filename of a wav file or "none" to play no sound when the reaction prompt is visible, or ``"none"``
``"showtimes_millis"``
     A list of milliseconds into the ``game`` step to make the reaction prompt visible and audible.
``"showtimes_trigger_counts"``
     A list of numbers to indicate which trigger pulses inside this step trigger this reaction prompt. A 1 in this list would trigger the reaction prompt to appear when the game receives the first trigger pulse after starting this ``game`` or ``game-adaptive`` step.
``"timeout_millis"``
     How many milliseconds the prompt should remain visible and audible once it appears if the player doesn't press the key to dismiss the prompt.
``"stay_visible"``
    ``false`` (default) or ``true``. A value of ``true`` indicates that the sound and image should continue to appear after the player presses the key corresponding to the prompt.
``"input_key"``
    Is the name of the keyboard key or mouse button the player should press in response to this reaction prompt. The options are in the list below.

::

    K_MOUSE1 -- Left mouse button
    K_MOUSE2 -- Middle mouse button
    K_MOUSE3 -- Right mouse button
    K_0 through K_9
    K_AMPERSAND
    K_ASTERISK
    K_AT
    K_BACKQUOTE
    K_BACKSLASH
    K_BACKSPACE
    K_BREAK
    K_CAPSLOCK
    K_CARET
    K_CLEAR
    K_COLON
    K_COMMA
    K_DELETE
    K_DOLLAR
    K_DOWN
    K_END
    K_EQUALS
    K_ESCAPE
    K_EURO
    K_EXCLAIM
    K_F1 through K_F15
    K_FIRST
    K_GREATER
    K_HASH
    K_HELP
    K_HOME
    K_INSERT
    K_KP0 through K_KP9
    K_KP_DIVIDE
    K_KP_ENTER
    K_KP_EQUALS
    K_KP_MINUS
    K_KP_MULTIPLY
    K_KP_PERIOD
    K_KP_PLUS
    K_LALT
    K_LAST
    K_LCTRL
    K_LEFT
    K_LEFTBRACKET
    K_LEFTPAREN
    K_LESS
    K_LMETA
    K_LSHIFT
    K_LSUPER
    K_MENU
    K_MINUS
    K_MODE
    K_NUMLOCK
    K_PAGEDOWN
    K_PAGEUP
    K_PAUSE
    K_PERIOD
    K_PLUS
    K_POWER
    K_PRINT
    K_QUESTION
    K_QUOTE
    K_QUOTEDBL
    K_RALT
    K_RCTRL
    K_RETURN
    K_RIGHT
    K_RIGHTBRACKET
    K_RIGHTPAREN
    K_RMETA
    K_RSHIFT
    K_RSUPER
    K_SCROLLOCK
    K_SEMICOLON
    K_SLASH
    K_SPACE
    K_SYSREQ
    K_TAB
    K_UNDERSCORE
    K_UP
    K_a through K_z

