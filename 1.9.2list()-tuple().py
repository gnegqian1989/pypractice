#!\usr\bin\python
#coding:utf-8

# list() 与tuple()  切换
t = (1,'23',[123,'abc'],('python','learn'))
tls = list(t)
print tls


t_tuple = tuple(tls)
print t_tuple
