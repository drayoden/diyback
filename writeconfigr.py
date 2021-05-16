import json


# note how all of this code is in the "with" scope below:
with open('./configr.json', 'r+') as f:
    d = json.load(f)

    d['lastfull'] = '20210506f'

    d['lastdiff'] = 1

    f.seek(0)
    json.dump(d, f, indent=2)
    f.truncate()

