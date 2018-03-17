# -*- coding: utf-8 -*-
from functools import reduce

# ll=[("zhangshan",10,"男"),("lisi",30,"男"),("王五",10,"女"),("chemin",20,"男")]
ll=[1,2,3]
reduce1 = reduce(lambda x, y: x[1] + y[1], ll)
print(reduce1)
