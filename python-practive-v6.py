#-*- coding:utf-8 -*-
import os
import sys
import  time

source = os.makedirs('/home/swaroop/byte','/home/swaroop/bin')
target_dir =  os.makedirs('/mnt/e/backup')
target =  target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % ('target, ''.join(source)')
if os.system(zip_command) == 0:
    print('Squccess backup to',target)
else:
    print('BAKCUP FAILED')


