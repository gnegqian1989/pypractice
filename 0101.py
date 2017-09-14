#!/usr/bin/python
# coding:utf-8
def printvalue(a,**d):
    print 'a=%d' %a
    for x in d:
        print x+'=%d' %d[x]

printvalue(1,b=2,c=3)
