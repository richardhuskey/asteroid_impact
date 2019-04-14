# Asteroid Impact (c) Media Neuroscience Lab, Rene Weber
# Authored by Nick Winters
# 
# Asteroid Impact is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
# 
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>. 
"""
Standard levels for Asteroid Impact

This script generates the standard levels and exports them as JSON files, including a level list.
"""
import json
from makelevel import make_level
from os import path

def export_levels(levelprefix='standard'):
    """Export standard levels and level-list JSON files"""
    leveldirectory = 'levels'
    levels = [# very slow ramp up in basic difficulty with no powerups
        make_level(seed=29873487, target_count=3, asteroid_count=1,
                   asteroid_speeds='slow', powerup_count=0),
        make_level(seed=49358743, target_count=5, asteroid_count=1,
                   asteroid_speeds='medium', powerup_count=0),
        make_level(seed=23423453, target_count=5,
                   asteroid_count=2, asteroid_speeds='medium', powerup_count=0),
        make_level(seed=34782342, target_count=8,
                   asteroid_count=3, asteroid_speeds='slow', powerup_count=0),
        ## introduce shield powerup
        make_level(seed=34782342, target_count=8,
                   asteroid_count=2, asteroid_speeds='medium',
                   powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
        make_level(seed=34782342, target_count=8,
                   asteroid_count=3, asteroid_speeds='medium',
                   powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
        ## introduce slow powerup
        make_level(seed=239487234, target_count=8, asteroid_count=3,
                   asteroid_speeds='medium',
                   powerup_count=10, powerup_types=['slow'], powerup_delay=0.5),
        make_level(seed=543245234, target_count=10, asteroid_count=2,
                   asteroid_speeds='fast',
                   powerup_count=10, powerup_types=['slow'], powerup_delay=0.5),

        # start mixing it up. These may get too difficult
        make_level(seed=134321432, target_count=10, asteroid_count=4,
                   asteroid_speeds='medium', asteroid_sizes='medium',
                   powerup_count=10, powerup_types=['slow', 'shield'],
                   powerup_delay=2.0),
        make_level(seed=234234234, target_count=10,
                   asteroid_count=4, asteroid_speeds='fast', asteroid_sizes='medium',
                   powerup_count=10, powerup_types=['slow', 'shield'],
                   powerup_delay=2.0),
        make_level(seed=983746598, target_count=10, asteroid_count=6,
                   asteroid_speeds='medium', asteroid_sizes='small',
                   powerup_count=10, powerup_types=['slow', 'shield'],
                   powerup_delay=2.0),
        make_level(seed=985623421, target_count=10, asteroid_count=8,
                   asteroid_speeds='medium', asteroid_sizes='varied',
                   powerup_count=10, powerup_types=['slow', 'shield'], powerup_delay=2.0),

        # crazy town
        # beatable in 10.3s using shields continuously
        make_level(seed=34782342, target_count=12, asteroid_count=5,
                   asteroid_speeds='extreme',
                   powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
        ]

    levelfiles = []
    for i, level in enumerate(levels):
        levelfilename = '%s%02d.json'%(levelprefix, i+1)
        levelfiles.append(levelfilename)
        # write level
        with open(path.join(leveldirectory, levelfilename), 'w') as levelfile:
            levelfile.write(json.dumps(level))

    # create level list json
    with open(path.join(leveldirectory, '%slevels.json'%levelprefix), 'w') as levelsfile:
        levellistobj = dict(levels=levelfiles)
        # pretty-print this json file because it's the most likely to be hand edited:
        levelsfile.write(json.dumps(levellistobj, indent=4, separators=(',', ': ')))

if __name__ == '__main__':
    export_levels()
