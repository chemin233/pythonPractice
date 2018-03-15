# -*- coding: utf-8 -*-
# 计算从1到某个值以内所有能被3或者17整除的数的和并输出

num=int(input("please input your number"))
i=0
sum=0
while i<num:
    i+=1
    if i%3==0 or i%17==0 :
        sum+=i
        print(i)
print(sum)