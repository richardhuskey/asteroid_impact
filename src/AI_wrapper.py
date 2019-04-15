import sys
import subprocess

path = "/Users/jacobfisher/Desktop/ai_s2018/src"
sys.path.insert(0, path)

subnum = eval(input("Subject number?"))
condition = eval(input("Condition?"))

log = "logs/%s_log.csv" % subnum
reactlog = "logs/%s_reactlog.csv" % subnum
condition_json = "condition%s.json" % condition

print(log)

subprocess.call([sys.executable, 'game.py', "--subject-number", str(subnum), "--script-json", str(condition_json), "--log-filename", str(log),"--display-mode", "windowed", "--reaction-log", str(reactlog), "--log-overwrite", "true"])
