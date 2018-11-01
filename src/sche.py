import gevent
 
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def sche():
	scheduler = BlockingScheduler()
	scheduler.add_job(func=aps_test, trigger='cron', second='*/2')
	scheduler.start()
 
def bar():
    print('.')
    gevent.sleep(0)
    print('#')
 
gevent.joinall([
    gevent.spawn(sche),
    gevent.spawn(bar),
])
