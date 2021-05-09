# import shutil
import tarfile as tf 
# import glob

# tar/compress folders and exclude files if needed
# use date/time name the file.

import time, datetime
from datetime import date


nowt = datetime.datetime.now()
now = str(date.today()).replace('-','') + '-' + str(nowt.hour) + str(nowt.minute) + str(nowt.second)
print(now)
source = ['/home/sysadm/Downloads/','/home/sysadm/Documents']
exclude = ['node_modules','cura','mfrc522']  
temp = '/home/sysadm/tmp/'
tgzfile = temp + now + '.tar.gz'

print('sources:')
for s in source:
    print('  --  ' + s)

print('excluded files and folders:')
for ef in exclude:
    print(' -- ' + ef)

def tarexclude(ti):
    for xname in exclude:
        if xname in ti.name:
            return None
    return ti

with tf.open(tgzfile, 'w:gz') as tar:
    for s in source:
        tar.add(s, filter=tarexclude)
    
 