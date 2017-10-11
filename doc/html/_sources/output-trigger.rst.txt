***************
Output Triggers
***************

Asteroid Impact can be configured to synchronize with external systems to notify them of certain game events over a serial port, or over a parallel port.

The configuration specifies whether to send to parallel or serial, which device to connect to, and a lookup of which game events to send notifications for, and what value to send for that event.

JSON Configuration Sample
=========================

This would go inside your configuration JSON, at the same level as the ``"steps"=[]`` list ::

    "output_trigger_settings": {
      "mode": "serial",
    
      "serial_trigger_strings_by_event": {
        "step_begin": "1",
        "game_death": "2",
        "game_level_complete": "3",
        "adaptive_difficulty_increase": "4",
        "adaptive_difficulty_decrease": "5"
      },
      "serial_options": {
        "port": "COM6",
        "baudrate": 19200
      },
    
      "parallel_trigger_hex_values_by_event": {
        "step_begin": "0x11",
        "game_death": "0x12",
        "game_level_complete": "0x14",
        "adaptive_difficulty_increase": "0x18",
        "adaptive_difficulty_decrease": "0x00"
      },
      "parallel_options": {
        "port_address_hex": "BF00",
        "common_data_value_hex": "0x10",
        "trigger_frames": 10
      }
    },


``"mode"`` Should be ``"none"`` to disable output triggers, ``"serial"``, or ``"parallel"``

The available game events are the following:

``"step_begin"``
    Occurs on the beginning of each step.
``"game_death"``
    When the player touches an asteroid during gameplay and dies. This works in both the game and adaptive gameplay steps.
``"game_level_complete"``
    When the player picks up the last crystal in a level in either the standard gameplay or adaptive gameplay steps.
``"adaptive_difficulty_increase"``
    When the player completes a level in the adaptive gameplay mode, and the "level score" increments to the next more difficult level in the list.
``"adaptive_difficulty_decrease"``
    When the player touches an asteroid and dies in the adaptive gameplay mode, and the "level score" decrements to the next less difficult level in the list.

Parallel-specific configuration and serial-specific configuration are described in their own sections below.

Serial Output Triggers
======================

When configured for serial output, the game will output the specified ascii-encoded string to the configured serial port on the frame the event happens.

If more than one event happens on the same frame, both strings are output. For example, in adaptive gameplay when the player dies the difficulty can increase on the same frame. When configured with the sample below ``N-`` will be sent over serial. ::

    "output_trigger_settings": {
      "mode": "serial",
    
      "serial_trigger_strings_by_event": {
        "step_begin": "N",
        "game_death": "D",
        "game_level_complete": "C",
        "adaptive_difficulty_increase": "+",
        "adaptive_difficulty_decrease": "-"
      },
      "serial_options": {
        "port": "COM6",
        "baudrate": 19200
      },
    },


The options for the ``serial_options`` are the following:

``"port"``
    This should be the device name of your serial port. In Windows it will likely be ``"COM1"`` or similar. Check Device Manager to find your serial port. In Linux it will likely be something like ``"/dev/ttyUSB0"``, and in OSX something like ``"/dev/tty.usbmodem1234"``
``"baudrate"``
    The baudrate in symbols/second to connect to the serial port. For hardware serial devices connecting at the wrong baudrate will result in gibberish characters being read.
``"bytesize"``
    Number of bits per byte. Defaults to 8, but it can sometimes be 7, 6 or 5.
``"stopbits"``
    Number of stop bits. Defaults to 1, can be 2.
``"parity"``
    The parity must be one of the following: ``"even"``, ``"mark"``, ``"names"``, ``"none"``, ``"odd"``, or ``"space"``.

Parallel Output
===============

Note: Parallel output only works on Windows computers, and they require the inpout32 driver to be installed.

Below is a sample script JSON with only serial output triggers configured and two text steps. ::

    "output_trigger_settings": {
      "mode": "parallel",

      "parallel_trigger_hex_values_by_event": {
        "step_begin": "0x11",
        "game_death": "0x12",
        "game_level_complete": "0x14",
        "adaptive_difficulty_increase": "0x18",
        "adaptive_difficulty_decrease": "0x00"
      },
      "parallel_options": {
        "port_address_hex": "BF00",
        "common_data_value_hex": "0x10",
        "trigger_frames": 10
      }
    },

The parallel output trigger mode will connect to a parallel port at the data address specified, and when the value in the status byte changes from the common to the trigger value will increment the current trigger count. See See :doc:`parallelport` for how to use the parallel port test feature to find the values and test. The values configured are in hexadecimal.

``parallel_options`` fields:

``"port_address_hex"``
    The IO port address for the parallel port. You can see this in Device Manager, go to properties for the parallel port, and on the Resources tab the first listed IO range address in hex is the one you should enter here.
``"common_status_value_hex"``
    The "inactive" value to wait for for the output register to while not outputting anything.
``"trigger_frames"``
    The number of 1/60s frames to hold the paralel port pins active. 10 would be about 160 milliseconds.

The hex value shown in the ``"parallel_trigger_hex_values_by_event"`` dictionary are what the output data pins would be set to if the one event happened on its own. For example, ``"step_begin": "0x11"`` would set D0 and D4 high (5v) and the other D pins low to notify of a step starting. By changing the trigger active value here, and the ``"parallel_options"``  ``"common_data_value_hex"`` you can configure your output to be either active-high or active low or even a mix of the two.

If multiple events occur on the same frame, such as ``"game_level_complete"`` and ``"adaptive_difficulty_increase"`` the bits *changed* from the ``"common_data_value_hex"`` are combined. For example, ``"common_data_value_hex":"0x10"``, ``"game_level_complete":"0x01"`` and ``"adaptive_difficulty_increase":"0x02"`` would write ``"0x03"`` to the data port when both happen on the same frame. This essentially wires the two different events to two different data pins, and sets the logic to be active high.

A second example, active low, would be ``"common_data_value_hex":"0x1F"``, ``"game_level_complete":"0x1E"`` and ``"adaptive_difficulty_increase":"0x1D"`` would write ``"0x1C"`` to the data port when both happen on the same frame.

A third example, mixed low/high would be ``"common_data_value_hex":"0x10"``, ``"game_level_complete":"0x01"`` and ``"adaptive_difficulty_increase":"0x00"`` would write ``"0x01"`` to the data port when both happen on the same frame.

