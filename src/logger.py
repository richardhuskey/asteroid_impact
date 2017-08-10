# Asteroid Impact (c) Media Neuroscience Lab, Rene Weber
# Authored by Nick Winters
# 
# Asteroid Impact is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>. 
"""CSV logger for AsteroidImpact game"""

import os
from sets import Set

def csv_escape(value):
    """return escaped and quoted as needed to be in a comma-separated CSV"""
    if ',' in value:
        # quote value
        return '"%s"'%value.replace('"', '""')
    return value


class AsteroidLogger(object):
    """Game state logger for AsteroidImpact game"""
    def __init__(self, filename, overwrite_file, max_asteroid_count = 12):
        """Create new AsteroidLogger"""
        # make output log file
        class NoneFile(object):
            """stub file for logging"""
            def write(self, data):
                """write nothing to no log file"""
                pass

        if filename:
            if os.path.exists(filename) and not overwrite_file:
                print 'Error: File "%s" exists and overwrite is not specified'%filename
                raise IOError('CSV Log file exists and overwrite not specified')
            self.logfile = open(filename, 'w')
        else:
            self.logfile = NoneFile()

        self.columns = [
            # Number for this research participant (subject).
            # This is specified on the command-line
            'subject_number',
            # Run number for this subject (specified on command-line)
            'subject_run',
            # milliseconds since application start
            'total_millis',
            # number of step in sequence, for example 1 for instructions then 2 for game
            'step_number',
            # milliseconds elapsed during this step. This resets to 0 on step change
            'step_millis',
            # of times trigger over serial or keyboard has been received on this step
            'step_trigger_count',
            # topmost screen name. Changes when mode change, but also inside of a mode
            # such as the level complete and game over screen.
            # instructions, gameplay, level_complete
            'top_screen',
            # game timer in milliseconds playing this level.
            # This starts negative for the countdown. Collisions and power-ups become active at 0
            'level_millis',
            # name of level JSON file
            'level_name',
            # score used for choosing level in game-adaptive mode
            'adaptive_level_score',
            # 1 for first attempt at this level, incrementing on each failure of the same level
            'level_attempt',
            # countdown, playing, completed or dead
            'level_state',
            # number of targets collected in this level
            'targets_collected',
            # center position of current target
            'target_x',
            'target_y',
            # the currently active powerup
            'active_powerup',
            # on-screen powerup
            # these shouldn't be trusted while a powerup is active because
            # active power-ups move around. A shield follows on top of the cursor
            # and the slow powerup moves offscreen.
            'powerup_x',
            'powerup_y',
            'powerup_diameter',
            'powerup_type',

            'cursor_x',
            'cursor_y',

            # question on current survey step
            'survey_prompt',
            # currently selected answer on current survey step
            'survey_answer',

            # reaction prompt state
            # only shows one active reaction prompts in per-frame log
            # use reaction prompt log for results when reaction prompts overlap in visibility
            'reaction_prompt_sound',
            'reaction_prompt_image',
            # reaction prompt state
            # blank: no active reaction prompt
            # "waiting": active reaction prompt is visible
            # "complete": player pressed button to dismiss reaction prompt
            # "timeout": player didn't press button in time
            'reaction_prompt_state',
            'reaction_prompt_millis'
            ]
            
        for i in xrange(1, max_asteroid_count+1):
            # asteroid columns
            prefix = ('asteroid_%d_' % i)
            self.columns.append(prefix + 'centerx')
            self.columns.append(prefix + 'centery')
            self.columns.append(prefix + 'diameter')

        self.columns_set = Set(self.columns)

        # write headers
        self.log({col:col for col in self.columns})

    def log(self, rowdict):
        """Save new log row for values in rowdict"""
        for i, key in enumerate(self.columns):
            if i > 0:
                self.logfile.write(',')
            if rowdict.has_key(key):
                self.logfile.write(csv_escape(str(rowdict[key])))
        self.logfile.write('\n')

        # validation: check for keys in rowdict that aren't in columns
        for key in rowdict.keys():
            if not key in self.columns_set:
                print 'key "%s" not in known list of columns. Not included in log'%key

class SurveyLogger(object):
    """Survey response logger for for AsteroidImpact game"""
    def __init__(self, filename, overwrite_file):
        """Create new SurveyLogger"""
        # make output log file
        class NoneFile(object):
            """stub file for logging"""
            def write(self, data):
                """write nothing to no log file"""
                pass

        if filename:
            if os.path.exists(filename) and not overwrite_file:
                print 'Error: File "%s" exists and overwrite is not specified'%filename
                raise IOError('CSV Survey Log file exists and overwrite not specified')
            self.logfile = open(filename, 'w')
        else:
            self.logfile = NoneFile()

        self.columns = [
            # Number for this research participant (subject).
            # This is specified on the command-line
            'subject_number',
            # Run number for this subject (specified on command-line)
            'subject_run',
            # milliseconds since application start
            'total_millis',
            # number of step in sequence, for example 1 for instructions then 2 for game
            'step_number',
            # milliseconds elapsed during this step. This resets to 0 on step change
            'step_millis',
            # of times trigger over serial or keyboard has been received on this step
            'step_trigger_count',
            # topmost screen name. Changes when mode change, but also inside of a mode
            # such as the level complete and game over screen.
            # instructions, gameplay, level_complete
            'top_screen',
            # question on current survey step
            'survey_prompt',
            # currently selected answer on current survey step
            'survey_answer',
            ]

        self.columns_set = Set(self.columns)

        # write headers
        self.log({col:col for col in self.columns})

    def log(self, rowdict):
        #hack test
        print 'surveylogger.log()'
        """Save new log row for values in rowdict"""
        for i, key in enumerate(self.columns):
            if i > 0:
                self.logfile.write(',')
            if rowdict.has_key(key):
                self.logfile.write(csv_escape(str(rowdict[key])))
        self.logfile.write('\n')

        # validation: check for keys in rowdict that aren't in columns
        for key in rowdict.keys():
            if not key in self.columns_set:
                print 'key "%s" not in known list of survey columns. Not included in log'%key

class ReactionLogger(object):
    """Reaction prompt logger for AsteroidImpact game"""
    def __init__(self, filename, overwrite_file):
        """Create new ReactionLogger"""
        # make output log file
        class NoneFile(object):
            """stub file for logging"""
            def write(self, data):
                """write nothing to no log file"""
                pass

        if filename:
            if os.path.exists(filename) and not overwrite_file:
                print 'Error: File "%s" exists and overwrite is not specified'%filename
                raise IOError('CSV Log file exists and overwrite not specified')
            self.logfile = open(filename, 'w')
        else:
            self.logfile = NoneFile()

        self.columns = [
            # Number for this research participant (subject).
            # This is specified on the command-line
            'subject_number',
            # Run number for this subject (specified on command-line)
            'subject_run',
            # milliseconds since application start
            'total_millis',
            # number of step in sequence, for example 1 for instructions then 2 for game
            'step_number',
            # milliseconds elapsed during this step. This resets to 0 on step change
            'step_millis',
            # of times trigger over serial or keyboard has been received on this step
            'step_trigger_count',
            # topmost screen name. Changes when mode change, but also inside of a mode
            # such as the level complete and game over screen.
            # instructions, gameplay, level_complete
            'top_screen',
            # game timer in milliseconds playing this level.
            # This starts negative for the countdown. Collisions and power-ups become active at 0
            'level_millis',
            # name of level JSON file
            'level_name',
            # score used for choosing level in game-adaptive mode
            'adaptive_level_score',
            # 1 for first attempt at this level, incrementing on each failure of the same level
            'level_attempt',
            # countdown, playing, completed or dead
            'level_state',
            
            # reaction prompt state
            'reaction_prompt_sound',
            'reaction_prompt_image',
            # blank: no active reaction prompt
            # "waiting": active reaction prompt is visible
            # "complete": player pressed button to dismiss reaction prompt
            # "timeout": player didn't press button in time
            'reaction_prompt_state',
            'reaction_prompt_millis'
            ]
            
        self.columns_set = Set(self.columns)

        # write headers
        self.log({col:col for col in self.columns})

    def log(self, rowdict):
        """Save new log row for values in rowdict"""
        for i, key in enumerate(self.columns):
            if i > 0:
                self.logfile.write(',')
            if rowdict.has_key(key):
                self.logfile.write(csv_escape(str(rowdict[key])))
        self.logfile.write('\n')

        # validation: check for keys in rowdict that aren't in columns
        for key in rowdict.keys():
            if not key in self.columns_set:
                print 'key "%s" not in known list of columns. Not included in log'%key
