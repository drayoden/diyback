import os

temp = '/home/sysadm/tmp/'
fn = '20210508-16120.tar.gz'
dest = 'gs://hex50/yoda'

os.system('gsutil mv ' + temp + fn + ' ' + dest)