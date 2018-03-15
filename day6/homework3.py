# -*- coding: utf-8 -*-

name_dic={}
info_dic={}

for i in range(3):
    name = input("please input your name:")
    phone = input("please input your phone:")
    addr = input("please input your addr:")
    info_dic["phone"]=phone
    info_dic["addr"]=addr
    name_dic[name]=info_dic
print(name_dic)

