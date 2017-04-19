******************
 Game Script JSON 
******************

AsteroidImpact will optionally run a sequence of modes specified in script.json. This can be used to advance the player between multiple lists of levels, with blank screens in between. Advancing to the next step happens after a specified duration, or for the instructions screen when the user clicks with the mouse.

Sample: ::

    {
        "trigger_settings": {
            "mode": "keyboard",
        
            "serial_options": {
                "port": "COM11",
                "baudrate": 19200,
                "trigger_byte_value" : 53
            },
        
            "keyboard_options" :
            {
                "trigger_key": "K_5"
            }
        },
        
        "steps":
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
            },
            {
                "action": "blackscreen",
                "duration": 5.0
            },
            {
                "action": "game-adaptive",
                "start_level": 0.5,
                "level_completion_increment": 0.5,
                "level_death_decrement": 0.6,
                "level_templates" : 
                [
                    {
                        "asteroid_count": 3,
                        "asteroid_sizes": "varied",
                        "asteroid_speeds": "medium",
                        "powerup_count": 10,
                        "powerup_delay": 0.5,
                        "powerup_types": [
                            "slow"
                        ],
                        "target_count": 10
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

You can visualize trigger pulses on screen by using the `--trigger-blink true` command-line option.

Sample trigger-driven JSON: ::

    {
        "trigger_settings": {
            "mode": "keyboard",
        
            "serial_options": {
                "port": "COM11",
                "baudrate": 19200,
                "trigger_byte_value" : 53
            },
        
            "keyboard_options" :
            {
                "trigger_key": "K_5"
            }
        },
        
        "steps": 
        [
            {
                "action": "instructions",
                "trigger_count": 10
            },
            {
                "action": "game",
                "levels": "levels/standardlevels.json",
                "trigger_count": 10
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
                "action": "game-adaptive",
                "trigger_count": 10,
                "start_level": 0.5,
                "level_completion_increment": 0.5,
                "level_death_decrement": 0.6,
                "level_templates" : 
                [
                    {
                        "asteroid_count": 3,
                        "asteroid_sizes": "varied",
                        "asteroid_speeds": "medium",
                        "powerup_count": 10,
                        "powerup_delay": 0.5,
                        "powerup_types": [
                            "slow"
                        ],
                        "target_count": 10
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

The serial trigger mode opens a serial port on the computer and when a byte is received with the value matching `trigger_byte_value` increases the trigger count. The `port` setting is the serial port, typically `COM1` through `COM16` on Windows, or `/dev/cu.usbmodem1234` or similar on OSX. If you have python and pyserial installed, you can list serial ports from the command-line by running `python -m serial.tools.list_ports` which will print out serial ports on your computer. You can also specify the `baudrate` for serial connections. The `trigger_byte_value` of 53 is the ASCII code for the character "5".

The keyboard trigger mode senses a trigger when the specified `trigger_key` is pressed down. `K_5` is the pygame constant for the "5" key. Multi-key trigger sequences are not supported. The availble options for `trigger_key` are the following: ::

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

Trigger Latency
===============

Depending on the computer being run, the trigger and other input sources has a bit of latency that will add some delay between when a trigger pulse is received and the game updates on screen. This was measured at under 0.1 seconds between sending a trigger pulse and the screen updating. This latency does not delay the scanner or device sending trigger pulses, so the overall timing should be similar, especially if the same hardware is used.

The latency has several factors:
* The game runs at 60hz so at best the average latency would be about 1/60s.
* Serial input is typically buffered on a computer for faster read rates.
* Graphic drawing is typically pipelined so there is enough work to do at once, and the drawing is completed before output to the screen (double buffering).
* Video scaling hardware in the LCD or projector will wait for receiving a full frame before scaling the image to the actual display element (LCD or mirrors in a projector)

Latency was measured as follows:
* Configure Arduino Leonardo as game trigger (sketch below) and to turn on LED when trigger pulse is sent. The basic stamp board based emulator also blinks an LED when it sends trigger pulses.
* Run game with `--trigger-blink true` command-line option
* Record 120FPS video using iPhone framed to show both LED on Arduino and trigger blink in lower right of game on screen
* Count frames between LED turning on (frame 0) and game showing blink (typically 9-13 frames at 120FPS). be careful that the video you're counting frames in is actually 120FPS and not the slow down/speed up effect the iPhone adds at the start/end.

Keyboard input latency was typically 2 frames shorter in the 120fps video, and Windows seemed to have a lower latency than OSX.

Serial Latency test sketch (Nearly any Arduino will work, tested with Leonardo, Uno) ::

    // Arduino Leonardo sketch to test latency of input trigger in serial
    // Blinks LED each time trigger pulse is sent over serial
    // Record video of LED with display of trigger pulse to measure latency
    #define DELAY_MILLIS 1000
    #define BLINK_MILLIS 100

    void setup() {
      // initialize serial communication at 19200 bits per second:
      Serial.begin(19200);
      pinMode(13, OUTPUT);
    }

    void loop() {
      delay(BLINK_MILLIS);
      digitalWrite(13, LOW);
      delay(DELAY_MILLIS-BLINK_MILLIS);
      Serial.print("5");
      Serial.flush();
      digitalWrite(13, HIGH);
    }

Keyboard Latency test sketch for Arduino Leonardo ::

    // Arduino Leonardo sketch to test latency of input trigger in keyboard mode
    // Blinks LED each time trigger pulse is sent over keyboard (5 number key is pressed)
    // Record video of LED with display of trigger pulse to measure latency
    #define DELAY_MILLIS 1000
    #define BLINK_MILLIS 100

    #include "Keyboard.h"

    void setup() {
      Keyboard.begin();
      pinMode(13, OUTPUT);
    }

    void loop() {
      // wait a few seconds before starting
      delay(10000);

      while (1) {
        Keyboard.press('5');
        digitalWrite(13, HIGH);

        delay(BLINK_MILLIS);
        
        Keyboard.releaseAll();
        digitalWrite(13, LOW);
        
        delay(DELAY_MILLIS - BLINK_MILLIS);
      }
    }

Common Step Attributes
======================

Each step has the following attributes:

 * action: The name of the action. Should be "instructions", "game", "text" or "blackscreen"
 * `duration`: The duration in seconds (such as 12.5) after which to automatically advance to the next step. This can be null for some actions, see below.


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
