# coding:utf-8

import gevent
from gevent import monkey
monkey.patch_all()

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def aps_test1():
    print ('test1')

def sche():
	scheduler = BlockingScheduler()
	scheduler.add_job(func=aps_test, trigger='cron', second='*/2')
	scheduler.add_job(func=aps_test1, trigger='cron', second='*/2')
	scheduler.start()
 
def bar():
	while 1:
		print('.')
		gevent.sleep(0)
		print('#')
 
gevent.joinall([
    gevent.spawn(sche),
    gevent.spawn(bar),
])
