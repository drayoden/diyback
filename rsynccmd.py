import json, os
import shutil

with open('./configr.json') as f:
    d = json.load(f)

# for source in d['sources']:
#     print(source['name'] + ' -- ' + source['path'])

# create exfile.txt:
with open('./exfile.txt','w') as exf:
    for exclude in d['excludes']:
        exf.write(exclude + '\r\n')

# "dest": "gs://hex50/yoda/",
#   "localarch": "/home/sysadm/.yodaback",
#   "gsutil": "/home/sysadm/google-cloud-sdk/bin/gsutil",
#   "lastback": 1,
#   "diffmax": 6

lastback = d['lastback']
diffmax = d['diffmax']
localarch = d['localarch']

print('lastback: ' + str(lastback))
print('diffmax: ' + str(diffmax))
print('localarch: ' + localarch)

# initial full backup
if (lastback == 0):
    archdest = 'full/'
    rsyncdiff = ''
    ++lastback
    if os.path.exists(localarch + archdest):
        print('purging: ' + localarch + archdest)
        shutil.rmtree(localarch + archdest)

# diff backup
if (lastback > 0 and lastback <= diffmax):
    archdest = 'd' + str(lastback) + '/'
    rsyncdiff = '--compare-dest=' + localarch + 'full/'
    ++ lastback
    if os.path.exists(localarch + archdest):
        print('purging: ' + localarch + archdest)
        shutil.rmtree(localarch + archdest)


# full backup (not initial)
if (lastback > diffmax):
    archdest = 'full/'
    rsyncdiff = ''
    lastback = 0
    if os.path.exists(localarch + archdest):
        print('purging: ' + localarch + archdest)
        shutil.rmtree(localarch + archdest)


rsyncprefix = 'rsync -a --exclude-from="./exfile.txt" '
rsyncsuffix = ' --delete-before'

# create local arch directories:
print('creating local archive directories:')

if not os.path.exists(localarch + archdest):
    print(localarch + archdest)
    os.mkdir(localarch + archdest)

for source in d['sources']:
    print(localarch + archdest + source['name'])
    try:
        os.mkdir(localarch + archdest + source['name'])
    except OSError as e:
        print(e)
        exit()

# create rsync command strings:
for source in d['sources']:
    rsyncsourcedest = source['path'] + ' ' + localarch + archdest + source['name']
    if not rsyncdiff == '':
        rsyncdiffdest = rsyncdiff + source['name'] + '/ '
    else:
        rsyncdiffdest = ''
    rsynccommand = rsyncprefix + rsyncdiffdest + rsyncsourcedest + rsyncsuffix
    print(rsynccommand)
    os.system(rsynccommand)



