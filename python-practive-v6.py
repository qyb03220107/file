#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
import os
import sys
import time

#try:
source = [ '/home/swaroop/byte','/home/swaroop/bin']
#except OSError:
#    pass
target_dir = ('/mnt/e/backup/')
today = target_dir + time.strftime("%Y%m%d")
now = time.strftime("H%M%S")
comment = input('Enter a comment --> ')
#添加时间的判断
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now  + '_' + comment.replace(' ','_') + '.zip'
if not os.path.exists(now):
    try:
        os.makedirs(today)
    except OSError:
        pass
    print("Successfuly created directory ",today)
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print ('Squccess backup to', target)
else:
    print('BAKCUP FAILED')
