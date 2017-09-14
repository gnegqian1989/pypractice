#!/usr/bin/python
#coding:utf-8
#列表的函数
        #extend append  追加函数
'''
la = [1,2,3]
lb = ['qiwair','python']
la.extend(lb)
print la
print lb

la = [1,2,3]
b = "abc"
la.extend(b)
print la
c= "5"
la.extend(c)
print la

one =["good","good","study"]
another = one.extend(["day","day","up"])
print one
print another

num_list = [1,2,3]
num_list.extend("8")
print num_list





lst = [1,2,3,4]
lst.append(["qiwsir","python","github"])
print lst
print len(lst)

lst.extend(["qiwsir","python"])
print lst
print len(lst)


         # hasattr() 用来判断 物体的属性是否存在
astr =[1,2]
print hasattr(astr,'__iter__')

a = 3
print hasattr (a,'__iter__')

a = 'b'
print hasattr(a,'__iter__')


         # count 某个元素在列表中出现的次数
la = [1,2,3,4,2,4,2]
print la.count(2)
la.append('a')
la.append('a')
print la
print la.count('a')
print la.count(5)



      #index 某个元素在列表中的位置
la = [1,2,3,4]
print la.index(3)

     # insert()  在列表中插入元素  insert(x,y) x:代表插入的位置从0开始  y：代表插入的内容
all_users  = ['python','github','io']
all_users.insert(0,'qwsir')
print all_users

length = len(all_users)
print length
all_users.insert(length,'algorithm')
print all_users

       #pop 和 remove 删除列表元素  pop（x）删除指定位置元素，如果没有参数则默认删除最后一个元素
       #                         remove可以删除指定元素
all_users = ['python','http://','qiwsir',]
print all_users
all_users.remove('http://')
print all_users

all_users = ['python','qiwsir','github','io','algorithm']
print "python" in all_users
if "python" in all_users:
    all_users.remove("python")
    print all_users
else:
    print "python is not in all_users"

if "python" in all_users:
    all.users.remove("python")
    print all_users
else:
    print "python is not in all_users"


all_users = ['python','qiwsir','github','io','algorithm']
print all_users
all_users.pop()
print all_users
print all_users.pop()

print all_users
all_users.pop(1)
print all_users
print all_users.pop(1)


           #reverse 把列表的元素顺序反过来
a = ['q','s','d','f','g','h']
a.reverse()
print a
'''

            #sort 对列表中的元素进行排序
a = [1,2,3,4,5,6]
a.sort()
print a

a.sort(reverse = True)
print a


lst =[ "python","a","java"]
lst.sort(key = len)
print lst


