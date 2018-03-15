# -*- coding: utf-8 -*-
import random

rand=random.randint(0,2)
# print(rand)
rule=["剪刀","shitou","bu"]
computer=rule[rand]
human=input("please input you rule:")
if human=="jiandao":
    if computer=="jiandao":
        print("这一局是平局")
    if computer=="石头":
        print("电脑赢!")