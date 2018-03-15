# -*- coding: utf-8 -*-

x = int(input("please input first Num"))
y = int(input("please input first Num"))
z = int(input("please input first Num"))

if (x == y == z):
    print("三个数相同")
elif x > y:
    if x > z:
        print("最大的数字:%d" % x)
    if x < z:
        print("最大的数字:%d" % z)
elif x == y:
    if x > z:
        print("最大的数字:%d" % x)
    if x < z:
        print("最大的数字:%d" % z)
else:
    if y > z:
        print("最大的数字:%d" % y)
    elif y == z:
        print("最大的数字:%d" % y)
    else:
        print("最大的数字:%d" % z)

