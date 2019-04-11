************
makelevel.py
************

makelevel.py
==================

makelevel.py is a python script to create new level JSON files for AsteroidImpact.

It requires Python 2.7 and PyGame 1.9.1

See :doc:`/leveljson` for format details of the generated level JSON files.

See :ref:`makelevel-creation-process` below for how levels are created.

.. _makelevel-creation-process:

======================
Creation Process
======================

The output of makelevel.py is a JSON file with positions for each crystal, power-up, and initial positions and directions for each asteroid. To run the same way repeatably, the game when running does not use any random number generator. Only makelevel.py which creates the level files uses a random number generator.

The random number generator used by makelevel.py starts with some initial internal state, called the seed, and generates a sequence of numbers which are manipulated into the required range. With the same seed, the random number generator will generate the same sequence of numbers. If the same seed, and other parameters are specified to makelevel.py then the output level JSON will be exactly the same. If for example you keep the seed and other parameters the same, but change the number of crystals the sequence of random numbers wouldn't generate the same asteroid positions because (as described below) the random numbers are used for crystals positions before asteroids positions and speeds.

If no seed is specified, the random number generator is seeded with the current time. This would give you a different position for crystals, asteroids and power-ups each time makelevel.py is run with the same arguments.

The seed can be changed to "re-roll" a level with the same settings until you are happy with the values randomly chosen by this script. I have generated levels with various seeds until getting the initial conditions I was looking for, such as no asteroids overlapping a crystal just after the level countdown ends, or intentionally creating a level where the first shield power-up overlaps an asteroid after the countdown ends.

The random numbers from the random number generator would typically come out as a uniform distribution between 0.0 and 1.0, but python exposes ways to convert these to a random integer in some range, for example 0 to 1223 inclusive to fit the X position of a crystal on screen, or a choice from a list of values such as this list of "medium" sizes: [110, 120, 150, 120, 140, 130].

This script creates levels as follows.

1. Initialize the random number generator with the supplied seed, or the current time if no seed is specified. 
2. Using the random number generator, choose random positions in the game area for the crystals to pick up.
3. Using the random number generator, choose random diameter (from list of options at specified size), speed, and location for each asteroid. Choosing a speed avoids finding purely horizontal or vertical movement by doing the following

   1. Choose maximum speed from list chosen by option.
   2. Find random integer for x movement and y movement ranging from 1 to speed, inclusive
   3. Find random sign for x and y movement.

4. Start the power-up list with a power-up delaying power-up if chosen in the options
5. Add each power-up, with a randomly chosen type from the list at a randomly chosen position. After each power-up add a power-up delaying power-up of the specified `--powerup-delay`.


Command-Line Options
==========================

The order of the command-line options does not matter.

Values (where applicable) come immediately after their command-line option. For example ``python makelevel.py --file samplefile.json``.

+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| Option                                            | Values                             | Default        | Description                                                                                                  |
+===================================================+====================================+================+==============================================================================================================+
| ``-h`` or ``--help``                              |                                    |                | Show help message and exit                                                                                   |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--file`` FILE                                   |                                    | [none]         | File to save level json to.                                                                                  |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--seed`` SEED                                   | integer                            | [current time] | Seed used to set initial state of random number generator. If none supplied will use current time.           |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--target-count`` TARGET_COUNT                   | integer                            | 5              | Number of crystals to pick up.                                                                               |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--asteroid-count`` ASTEROID_COUNT               | integer                            | 5              | Number of asteroids to avoid.                                                                                |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--asteroid-sizes`` {small,medium,large,varied}  | one of {small,medium,large,varied} | large          | Approximate size of asteroids.                                                                               |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--asteroid-speeds`` {slow,medium,fast,extreme}  | one of {slow,medium,fast,extreme}  | slow           | Approximate speed of asteroids.                                                                              |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--powerup-count`` POWERUP_COUNT                 | integer                            | 5              | Number of distinct power-ups to create for the player to pick up.                                            |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--powerup-initial-delay`` POWERUP_INITIAL_DELAY | float                              | 0.0            | Delay in seconds before first powerup is available.                                                          |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--powerup-delay`` POWERUP_DELAY                 | float                              | 1.0            | Delay in seconds after powerup is used before next one becomes available.                                    |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
| ``--powerup-types`` {shield,slow,all,none}        | one of {shield,slow,all,none}      | all            | Types of powerups that are in level.                                                                         |
+---------------------------------------------------+------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------+
