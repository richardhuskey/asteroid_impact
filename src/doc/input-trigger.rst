**************
Input Triggers
**************

Asteroid Impact can be configured to synchronize advancing steps with pulses from an external system. The external system should either send a byte over serial to the computer running Asteroid Impact, appear as a keyboard and press a key, or change the logic level of at least one parallel status pin. Each of these events is seen as a incoming trigger pulse, and steps in Asteroid Impact advance after a configurable number of pulses.

You can visualize trigger pulses with an icon that flashes on screen by using the ``-–trigger-blink true`` command-line option.

Input Triggers
==============

The input triggers will automatically advance to the next step after the game receives the configured number of trigger pulses. The trigger pulse count for each step is configured with the ``trigger_count`` attribute.

The input triggers can be configured for one of the the three inputs:

 1. When receiving a particular byte, such as an ascii '5' over a serial port.
 2. When a keyboard key, like the 5 number key is pressed down.
 3. When the input on configured parallel port changes the status byte value from the configured common value to the configured trigger value.


JSON Configuration Sample
=========================

Below is a sample script JSON with input triggers configured. ::

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
          "title": "Additional Instructions",
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

Serial Input Configuration
==========================

When configured for serial input, the game connects to the serial port with the specified options and reads all input. When the game receives a byte that matches ``trigger_byte_value`` configuration it treats that as a trigger input. Other bytes are read but ignored.

Below is a sample script JSON with only serial input triggers configured and two text steps. ::

    {
      "trigger_settings": {
        "mode": "keyboard",

        "serial_options": {
          "port": "COM5",
          "baudrate": 19200,
          "trigger_byte_value": 53
        }
      },
      "steps": [
        {
          "action": "text",
          "text": "Text step 1"
          "title": "",
          "trigger_count": 10
        },
        {
          "action": "text",
          "text": "Text step 2"
          "title": "",
          "trigger_count": 10
        }
      ]
    }


``serial_options`` options:

``trigger_byte_value``
    The decimal representation of the byte you want to trigger on. In the sample above, the ``trigger_byte_value`` of 53 is the '5' character in ASCII. See http://www.asciitable.com the 'Dec' colum shows the decimal number of the character.
``port``
    This should be the device name of your serial port. In Windows it will likely be ``"COM1"`` or similar. Check Device Manager to find your serial port. In Linux it will likely be something like ``"/dev/ttyUSB0"``, and in OSX something like ``"/dev/tty.usbmodem1234"``
``baudrate``
    The baudrate in symbols/second to connect to the serial port. For hardware serial devices connecting at the wrong baudrate will result in gibberish characters being read.
``bytesize``
    Number of bits per byte. Defaults to 8, but it can sometimes be 7, 6 or 5.
``stopbits``
    Number of stop bits. Defaults to 1, can be 2.
``parity``
    The parity must be one of the following: ``"even"``, ``"mark"``, ``"names"``, ``"none"``, ``"odd"``, or ``"space"``.

Keyboard Input
==============
Below is a sample script JSON with only keyboard input triggers configured and two text steps. ::

    {
      "trigger_settings": {
        "mode": "keyboard",

        "keyboard_options": {
          "trigger_key": "K_5"
        },
      },
      "steps": [
        {
          "action": "text",
          "text": "Text step 1"
          "title": "",
          "trigger_count": 10
        },
        {
          "action": "text",
          "text": "Text step 2"
          "title": "",
          "trigger_count": 10
        }
      ]
    }

The trigger pulse is when you press down the configured ``trigger_key``. ``"K_5"`` corresponds to the 5 key on your keyboard.

There is not currently an option to trigger on joystick buttons, or mouse buttons. Only keyboard right now.

Multi-key trigger sequences are not supported. The availble options for ``trigger_key1`` are the following: ::

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



Parallel Input
==============

Note: Parallel input only works on Windows computers, and they require the inpout32 driver to be installed.

Below is a sample script JSON with only serial input triggers configured and two text steps. ::

    {
      "trigger_settings": {
        "mode": "parallel",

        "parallel_options": {
          "port_address_hex": "BF00",
          "common_status_value_hex": "0x00",
          "trigger_status_value_hex": "0x08"
        }
      },
      "steps": [
        {
          "action": "text",
          "text": "Text step 1"
          "title": "",
          "trigger_count": 10
        },
        {
          "action": "text",
          "text": "Text step 2"
          "title": "",
          "trigger_count": 10
        }
      ]
    }

The parallel trigger mode will connect to a parallel port at the data address specified, and when the value in the status byte changes from the common to the trigger value will increment the current trigger count. See See :doc:`parallelport` for how to use the parallel port test feature to find the values and test. The values configured are in hexadecimal.

``parallel_options`` fields:

``port_address_hex``
    The IO port address for the parallel port. You can see this in Device Manager, go to properties for the parallel port, and on the Resources tab the first listed IO range address in hex is the one you should enter here.
``common_status_value_hex``
    The "off" value to wait for for the status register to return to before the next trigger.
``trigger_status_value_hex``
    The "active" value to wait for on the status register that indicates a trigger pulse. 

The parallel port triggers have common/trigger values configured independently so that you can configure both active high and active low, or status pins that are inverted (11/busy).

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
* Run game with ``--trigger-blink true`` command-line option
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

