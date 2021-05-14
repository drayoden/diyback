#!/usr/bin/env python

import json, os
import time, datetime
from datetime import date
import tarfile as tf 

# open config file...
try:
    with open('./config.json') as f:
        d = json.load(f)
        print('config file opened sucessfully...')
except:
    print('oops! cannot open config file...')

# create lists from config file settings
sources  = d['sources']
excludes = d['excludes']
destination = d['dest']
temp = d['temp']

# print(sources)
# print(excludes)
# print(destination)
# print(temp)

# verify temp location...
# dumb thing: 'isdir' does not throw an exception so a try block cannot be used.
if (os.path.isdir(temp)):
   print('temp location: [' + temp + ']')
else:
    print('temp location [' + temp + '] does not exist...')
    print('creating temp location...')
    try: 
        (os.mkdir(temp))
        print('temp location created succefully...')
    except:
        print('could not create temp location: [' + temp + ']')
        exit()

# verify the backup destination...
if (os.system('gsutil -q stat ' + destination) == 0 ):
    print('archive destination: [' + destination + ']')
else:
    print('archive destination [' + destination + '] does not exist...' )
    print('exit on error: verify archive destination and rerun...')
    exit()

# set the filename of the archive file...
nowt = datetime.datetime.now()
now = str(date.today()).replace('-','') + '-' + str(nowt.hour) + str(nowt.minute) + str(nowt.second)

tgzfile = now
tgzfile = '20210514-113659'

# open backup log file...
try:
    lfile = open(temp + tgzfile + '.log', 'w+')
    print('log file created: ' + temp + tgzfile + '.log')
except:
    print('could not create log file...')

# exclude filter for tar file creation... 
def tarexclude(ti):
    for xname in excludes:
        if xname in ti.name:
            lfile.write('- ' + ti.name + '\r\n')
            return None
    lfile.write('+ ' + ti.name + '\r\n')
    return ti

# open the tar.gz file in the temp location... 
print('creating local archive file: ' + temp + tgzfile + '.tar.gz')
with tf.open(temp + tgzfile + '.tar.gz', 'w:gz') as tar:
    for s in sources:
        tar.add(s, filter=tarexclude)

# move the file to the gcs
print('moving archive file and log to gcs...')
os.system('gsutil -m mv ' + temp + tgzfile + '* ' + destination)

print('backup completed successfully...')





