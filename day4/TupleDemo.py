# -*- coding: utf-8 -*-
# aa=input("please input a string:")
# upperString=aa.upper();
# print(list(upperString))

height=int(input("please input the height:"))
distence=height
count=1
while True:
    count+=1
    height/=2
    distence +=2* height
    if count==10:
        print("distence---", distence)
    if count == 20:
        print("distence---", distence)
        break
