# -*- coding: utf-8 -*-
line=0
while line<10:
    column = 0
    while column<line:
        column+=1
        print(column,"*",line,"=",column*line,end="  ")
    print("",end="\n")
    line += 1