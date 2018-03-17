# -*- coding: utf-8 -*-
countNum = 0
while countNum < 3:
    countNum += 1
    password = input("please input your password:")
    if password == "888888":
        while True:
            mony = int(input("please input how much mony:"))
            if mony % 100 == 0 and 1000 >= mony > 0:
                print(mony)
                break
            else:
                continue
        print("commplete!")
        break
