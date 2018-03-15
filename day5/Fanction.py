# -*- coding: utf-8 -*-
import math


def my_abs(x):
    if x>=0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b,(int, float)) and isinstance(c, (int, float))):
        raise TypeError("bad operand type")
    if a == 0:
        print("x的解是:", -c/b)
    else:
        if (b*b-4*a*c)>=0:
            x1=(-b+math.sqrt(b*b-4*a*c)/2*a)
            x2=(-b-math.sqrt(b*b-4*a*c)/2*a)
            print(x1, x2)
        else:
            print("此方程无解")
