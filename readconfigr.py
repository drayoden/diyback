import json

with open('./configr.json') as f:
    d = json.load(f)

for source in d['sources']:
    print(source['name'] + ' -- ' + source['path'])

for exclude in d['excludes']:
    print(exclude)

print(d['dest'])
print(d['temp'])
print(d['gsutil'])
print(d['lastfull'])
print(d['lastdiff'])
print(d['diffbacks'])




