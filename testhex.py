import datetime as datetime
from datetime import date

groupprefix = 'fG'
# groupprefix = 'dG'
backupgroup = 56

nowt = datetime.datetime.now()
groupnumber = '{:02x}'.format(backupgroup).upper()
# archfilename = str(date.today()).replace('-','') + '_' + str(nowt.hour) + str(nowt.minute) + str(nowt.second) + '_' + groupprefix + groupnumber
archfilename = nowt.strftime("%Y%m%d_%H%M") + '_' + groupprefix + groupnumber
print(archfilename)





# for x in range(0,256):
#     y = '0x' + '{:02x}'.format(x).upper()
#     print(y)