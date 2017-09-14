#!/sur/bin/python
#coding:utf-8
#序列的基本操作
'''
#cmp 比较大小 cmp(x,y)   x>y 1,  x<y  -1,   x=y 0
print "cmp(80,100):",cmp(80,100)
print "cmp(180,100):",cmp(180,100)
print "cmp(-80,100)",cmp(-80,100)
print "cmp(80,-100)",cmp(80,-100)
print "cmp(80,80)",cmp(80,80)


#len() 字符长度及个数
lst = ['python','java','c++']
print len(lst)


# + 连接两个序列
lst = ['python','java','c++']
alst = [1,2,3,4,5]
print lst + alst

'''
#*重复元素
lst = ['python','java','c++']
print lst*3


# in
print "python" in lst
print "c" in lst

#max() min()
alst =[1,2,3,4,5,6]
print max(alst)
print min(alst)
print max(lst)
print min(lst)

