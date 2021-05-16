import tarfile as tf 
import time, datetime
from datetime import date

nowt = datetime.datetime.now()
now = str(date.today()).replace('-','') + '-' + str(nowt.hour) + str(nowt.minute) + str(nowt.second)
print(now)

# source for non-rsync test:
# source = ['/home/sysadm/Downloads/','/home/sysadm/Documents']

# source for rsync test: 
source = '/home/sysadm/.yodaarch/full/'

# excludes are not use for rsync version:
# exclude = ['node_modules','cura','mfrc522']  


# temp = '/home/sysadm/tmp/'

# rsync version: create/delete this folder for each backup:
temp = '/home/sysadm/.yodaarch/tmp/'

tgzfile = temp + now + '.tar.gz'

# rsync:
print('sources:')
print('  --  ' + source)


# non-rsync:
# print('sources:')
# for s in source:
#     print('  --  ' + s)

# excludes only used for non-rsync process:
# print('excluded files and folders:')
# for ef in exclude:
#     print(' -- ' + ef)

# exclude filter is not needed for rsync version:
# def tarexclude(ti):
#     for xname in exclude:
#         if xname in ti.name:
#             return None
#     return ti

# non-rsync version:
# with tf.open(tgzfile, 'w:gz') as tar:
#     for s in source:
#         tar.add(s, filter=tarexclude)
    
# rsync version:
with tf.open(tgzfile, 'w:gz') as tar:
    tar.add(source)


 