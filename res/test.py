import json

f = open('FlyMission.json','r+')
l = json.load(f)
print(l)
