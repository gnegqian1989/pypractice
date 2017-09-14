#!/usr/bin/python
# coding:utf-8


  # split() 将字符串分割为列表
line = "hello.I am qiwsir.Welcome you"
b = line.split(".")
print b

name  = "Albert Ainstain"
c = name.split(" ")
print c

s = "I am,writing\npython\tbook on line"
print s
a = s.split()
print a

#  \n 换行 \t  tab 缩进

# join() split的逆运算
name = ['Albert','Ainstain' ]
d = "".join(name)
print d
e = ",,".join(name)
print e

s = "I am, writing\npython\tbook on line"
print s
f = s.split()
print f
g = " ".join(f)
print g
h = g.split()
print h


 