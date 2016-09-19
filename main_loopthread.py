#!/usr/bin/env python

import threading
from time import sleep

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
	n += 1
	print('thread %s >>> %s' % (threading.current_thread().name, n))
	sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
