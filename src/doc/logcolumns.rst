***********
Log Columns
***********

This page describes each column in the saved log CSV.

Game Coordinates
======================

The sizes, speeds, and positions in this file are specified in game coordinates, not pixels. This allows the screen resoloution to change but the game objects will still move and appear in the same way relative to each other.

The game play area is 1280 units wide, 896 units tall. The top left is at x=0, y=0 and bottom right at x=1280, y=960. The center of the screen is x=640, y=480.


.. _log-columns-label:

Log Columns
================

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Log Column             | Description                                                                                                                                                                           |
+========================+=======================================================================================================================================================================================+
| subject_number         | Number for this research participant (subject). This is specified on the command-line.                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| subject_run            |   Run number for this subject. This is specified on the command-line.                                                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| total_millis           |  Milliseconds since application start.                                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_number            |  Number of step in sequence, for example 1 for instructions then 2 for game.                                                                                                          |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_millis            |  Milliseconds elapsed during this step. This resets to 0 on step change.                                                                                                              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_trigger_count     |  Number of times trigger over serial or keyboard has been received on this step.                                                                                                      |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| top_screen             |  Topmost screen name. Changes when mode change, but also inside of a mode such as the level complete and game over screen. Some values are instructions, gameplay and level_complete. |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_millis           | Game timer in milliseconds playing this level. This starts negative for the countdown. Collisions and power-ups become active at 0.                                                   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_name             |  Name of level JSON file.                                                                                                                                                             |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| adaptive_level_score   |  Score used for choosing level in game-adaptive mode.                                                                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_attempt          | 1 for first attempt at this level, incrementing on each failure of the same level.                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_state            | The state of the current level. countdown, playing, completed or dead.                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| targets_collected      | Number of targets collected in this level.                                                                                                                                            |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| target_x               | Center position of current target.                                                                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| target_y               | Center position of current target.                                                                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| active_powerup         | The currently active powerup type.                                                                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| powerup_x              | on-screen powerup center's X position. See note below about how this changes while powerup is ctive.                                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| powerup_y              | on-screen powerup center's Y position. See note below about how this changes while powerup is active.                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| powerup_diameter       | on-screen powerup diameter. See note below about how this changes while powerup is active.                                                                                            |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| powerup_type           | on-screen powerup type.                                                                                                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cursor_x               | X-coordinate of the player's cursor.                                                                                                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cursor_y               | Y-coordinate of the player's cursor.                                                                                                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_sound  | Configured sound for currently visible reaction prompt.                                                                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_image  | Configured image for currently visible reaction propmt.                                                                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_state  | Status of active reaction time prompt (waiting, complete, timeout, timeout_step_end), or blank if none.                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_millis | Milliseconds that reaction prompt has been active for, or blank if none.                                                                                                              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| survey_prompt          | The survey question shown on the current survey question screen.                                                                                                                      |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| survey_answer          | The currently selected survey answer on the current survey question screen.                                                                                                           |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| asteroid_N_centerx     | X-coordinate of asteroid at position N. N starts at 1.                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| asteroid_N_centery     | Y-coordinate of asteroid at position N. N starts at 1.                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| asteroid_N_diameter    | Diameter of asteroid at position N. N starts at 1.                                                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Position of active powerups
===========================

When activated, powerups move depending on their effect.

The shield powerup will follow on top of the player's cursor.

The slow powerup teleports off screen so it's no longer visible.

These mean that the x/y position of the currently visible powerup
don't mean the same thing when the powerup is active.

Reaction Prompts
================

When there is an active (visible or audible) reaction prompt, the state wil change from blank to "waiting". If the player presses the corresponding button the state will change to "complete". Otherwise, on the frame the prompt disappears the state changes to "timeout". If the step ends before the reaction prompt is completed or times out naturally the state changes to "timeout_step_end"

``reaction_prompt_millis`` is the time since the prompt appeared.

Reaction Prompts Log Columns
-----------------------------
For the reaction prompt log CSV, the columns are a subset of those for the per-frame log as shown below.

New rows for the reaction prompt CSV are only added when a reaction prompt is completed in time, times out, or the step changes.

To output a reaction prompt log file use the ``--reaction-log-filename FILENAME`` command-line option. 

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Log Column             | Description                                                                                                                                                                           |
+========================+=======================================================================================================================================================================================+
| subject_number         | Number for this research participant (subject). This is specified on the command-line.                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| subject_run            |   Run number for this subject. This is specified on the command-line.                                                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| total_millis           |  Milliseconds since application start.                                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_number            |  Number of step in sequence, for example 1 for instructions then 2 for game.                                                                                                          |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_millis            |  Milliseconds elapsed during this step. This resets to 0 on step change.                                                                                                              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_trigger_count     |  Number of times trigger over serial or keyboard has been received on this step.                                                                                                      |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| top_screen             |  Topmost screen name. Changes when mode change, but also inside of a mode such as the level complete and game over screen. Some values are instructions, gameplay and level_complete. |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_millis           | Game timer in milliseconds playing this level. This starts negative for the countdown. Collisions and power-ups become active at 0.                                                   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_name             |  Name of level JSON file.                                                                                                                                                             |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| adaptive_level_score   |  Score used for choosing level in game-adaptive mode.                                                                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_attempt          | 1 for first attempt at this level, incrementing on each failure of the same level.                                                                                                    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| level_state            | The state of the current level. countdown, playing, completed or dead.                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_sound  | Configured sound for currently visible reaction prompt.                                                                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_image  | Configured image for currently visible reaction propmt.                                                                                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_state  | Status of active reaction time prompt (waiting, complete, after_complete, timeout, timeout_step_end), or blank if none.                                                               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| reaction_prompt_millis | Milliseconds that reaction prompt has been active for, or blank if none.                                                                                                              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Survey Question
===============

When the current step is a survey question screen, the question and selected answer are logged.

Survey Answer Log Columns
-------------------------
For the survey question response CSV, the columns are a subset of those for the per-frame log as shown below.

New rows are only added when the step is advanced, so the log will only include the option selected when the step switched not a history of every option they clicked on.

To output a survey question answer log file use the ``--survey-log-filename FILENAME`` command-line option. 

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Log Column             | Description                                                                                                                                                                           |
+========================+=======================================================================================================================================================================================+
| subject_number         | Number for this research participant (subject). This is specified on the command-line.                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| subject_run            |   Run number for this subject. This is specified on the command-line.                                                                                                                 |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| total_millis           |  Milliseconds since application start.                                                                                                                                                |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_number            |  Number of step in sequence, for example 1 for instructions then 2 for game.                                                                                                          |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_millis            |  Milliseconds elapsed during this step. This resets to 0 on step change.                                                                                                              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step_trigger_count     |  Number of times trigger over serial or keyboard has been received on this step.                                                                                                      |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| top_screen             |  Topmost screen name. Changes when mode change, but also inside of a mode such as the level complete and game over screen. Some values are instructions, gameplay and level_complete. |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| survey_prompt          | The survey question shown on the current survey question screen.                                                                                                                      |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| survey_answer          | The currently selected survey answer on the current survey question screen.                                                                                                           |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Asteroid Numbers
================

The ``asteroid_N_centerx``, ``asteroid_N_centery`` and ``asteroid_N_diameter`` columns are numbered by the position of the asteroid in the game's list of asteroids.

For the standard gameplay, the index of the asteroid in the list is the same as in the level JSON file.

For adaptive gameplay, when increasing the number of asteroids they are added to the end of the list. When decreasing the number, they are removed (after scaling to zero over about a second) from the end of the list.

The ``N`` in the column counts from 1, up to the maximum number of asteroids in any level of either mode. If there aren't that many asteroids in the current mode, or current level, the values for the remaining columns will be blank.
