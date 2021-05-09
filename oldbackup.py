#!/usr/bin/env python3

#- backup.py
#- Daryn Oden (HEX50 LLC)

#- parse date for new filename
#- find, confirm usb data drive

import os, shutil
import socket, tarfile
import time, datetime
from datetime import date
from os import listdir

nowt = datetime.datetime.now()
now = str(date.today()).replace('-','') + str(nowt.hour) + str(nowt.minute) + str(nowt.second)
usr = os.environ['USERNAME']
hm = os.environ['HOME'] + '/'
hostn = socket.gethostname()

#- check if temp directory exists...

if (not os.path.exists(hm+"temp/")):
	r = input("temp folder does not exist; create? ").lower()
	if r == 'y':
		os.makedirs(hm+"temp/")
	else:
		quit()


print('~' * 30)
print("date: %s" %(now))
print("user: %s" %(usr))
print("home: %s" %(hm))
print("hostname: %s" %(hostn))
print('~' * 30)

usbdir = "/media/" + usr
dirlist = ("Downloads","Documents",".local/bin/backup.py","/media/sysadm/data/proj")
mb = 1000000

def main():
	usb = getusb()
	if usb:
		usbp = usbdir + '/' + usb + '/'
		print("usb path: %s" %(usbp))
		fname = hostn + '.' + now + '.tar.gz'
		print("filename: %s" %(fname))
		r = input("continue? y/n " ).lower()
		if r == 'y':
			print("backup in progress...")
			with tarfile.open(hm+"temp/"+fname,"w:gz") as tar:
				for n in dirlist:
					print("adding [%s]"%(n))
					if n[0] == '/':
						tar.add(n)
					else:
						tar.add(hm + n)
			print("backup complete...")
			print("moving file to usb...")
			shutil.move(hm+"temp/"+fname,usbp)
			print("file moved successfully...")

	else: 
		print("usb device not available...")
			


def getusb():
	dirs = os.listdir(usbdir)
	for d in dirs:
		st = os.statvfs(usbdir + '/' + d + '/')
		bytefree = st.f_bavail * st.f_bsize
		mbfree = bytefree/mb
		r = input("\tUse %s [%.2f MB free] ? y/n: " %(d,mbfree)).lower()
		if r == 'y':
			return d
	return False

if __name__ == '__main__':
    main()
