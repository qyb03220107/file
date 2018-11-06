#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time

#try:
source = [ '/home/swaroop/byte','/home/swaroop/bin']
#except OSError:
#    pass
target_dir = ('/mnt/e/backup')
today = target_dir + time.strftime("-%Y%m%d")
now = time.strftime("H%M%S")
if not os.path.exists(now):
    try:
        os.mkdir(today)
    except OSError:
        pass
    print("Successfuly created directory ",today)
print (target_dir)
target = today +  os.sep  +  now  + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print ('Squccess backup to', target)
else:
    print('BAKCUP FAILED')
