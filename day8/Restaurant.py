# -*- coding: utf-8 -*-
class Restaurant:
    # 采用实例变量.属性名的方式  修改类变量和修改实例变量的不同

    restaurant_add = "zhangting"

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name==", self.restaurant_name, "pengren==", self.cuisine_type)

    def open_restaurant(self):
        print("餐馆正在营业")

    def setAdd(self):
        self.restaurant_add = "shanghai"

    def getAdd(self):
        return self.restaurant_add

    def getAdd(self):
        return self.restaurant_name

    def setAdd(self, add):
        self.restaurant_add = add


# chemindain.open_restaurant()
# chemindain.describe_restaurant()
# print("------------------------------")
# print(Restaurant.restaurant_add)
# chemindain.restaurant_add="beijing"
# print("实例对象:",chemindain.restaurant_add)
# print("类名:",Restaurant.restaurant_add)

# chemindain.setName()
# print("实例对象:",chemindain.restaurant_add)
# print("类名:",Restaurant.restaurant_add)
# print(getattr(chemindain,"restaurant"))
# chemindain=Restaurant("chemin","zhongchan")
# print(chemindain.getAdd())
# print(chemindain.restaurant_name)
# print("------------------------------")
#
# chemindain.restaurant_add="sichuan"
# print(chemindain.restaurant_add)
# name = chemindain.getAdd()
# print(name)

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def show(self):
        print(" fjfkdsla;fjd;lsa",self.flavors)

ice=IceCreamStand("chemin","cuendn","口味")
ice.show()