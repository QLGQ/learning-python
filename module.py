#!/usr/bin/env python2
#-*-coding:utf-8-*-

'a test module'

_author_='Qiang Wu'

import sys

def test():
    args = sys.argv
    if len(args) == 1 :
       print('Hello,world!')
    elif len(args) == 2 :
       print('Hello,%s!' % args[1])
    else:
       print('Too many arguments!')

#if _name_ == '_main_':
#print(test())
test()
