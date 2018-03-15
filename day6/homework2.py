# -*- coding: utf-8 -*-

list1=[]
list2=[]
while True:
    num =int(input("please input your number,input 0 exit:"))
    if num==0:
        break
    else:
        list1.append(num)
print(list1)
index_list= (range(len(list1)+1))[::2]
print(index_list)
for x in index_list:
    print(x)
    if x==0:
        continue
    list2.append(list1[x-1]-list1[x-2])

print(list2)