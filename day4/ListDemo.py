# -*- coding: utf-8 -*-
# print([(x,y) for x in range(1,5) for y in range(1, 5)])
names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
#注意遍历顺序，这是实现的关键 
bb=[name for lst in names for name in lst if name.count('e')>=2]
print(bb)