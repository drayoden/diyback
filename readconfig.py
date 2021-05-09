import json

with open('./config.json') as f:
    d = json.load(f)

source = d['sources']
exclude = d['excludes']
dest = d['dest'][0]

for x in source:
    print(x)

for y in exclude:
    print(y)

print(dest)

