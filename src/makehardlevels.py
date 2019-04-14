'''
Standard levels for Asteroid Impact
This script generates the standard levels and exports them as json files, including a level list.

'''
import json
from makelevel import make_level
from os import path

def export_levels(levelprefix='hard'):
	leveldirectory = 'levels'
	levels = [
		# crazy town
		# beatable in 10.3s using shields continuously
		make_level(seed=34782342, target_count=12, asteroid_count=5, asteroid_speeds='extreme', 
			powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
		make_level(seed=234325342, target_count=12, asteroid_count=5, asteroid_speeds='extreme', 
			powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
		make_level(seed=463345434, target_count=12, asteroid_count=5, asteroid_speeds='extreme', 
			powerup_count=10, powerup_types=['shield'], powerup_delay=0.5),
		]
	
	levelfiles = []
	for i,level in enumerate(levels):
		levelfilename = '%s%02d.json'%(levelprefix,i+1)
		levelfiles.append(levelfilename)
		# write level 
		with open(path.join(leveldirectory,levelfilename),'w') as f:
			f.write(json.dumps(level))
	
	# create level list json
	with open(path.join(leveldirectory,'%slevels.json'%levelprefix),'w') as f:
		levellistobj = dict(levels=levelfiles)
		# pretty-print this json file because it's the most likely to be hand edited:
		f.write(json.dumps(levellistobj, indent=4, separators=(',',': ')))

if __name__ == '__main__':
	export_levels()
