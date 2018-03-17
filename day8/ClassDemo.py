# -*- coding: utf-8 -*-
class Student():
    height=10
    def __init__(self, name, sex):
        super().__init__()
        self.name = name;
        self.sex = sex;

    def move(self,speed,add):
        print(self.name, self.height,speed,add,"run fast!")


chemin = Student("chemin", "男")
chemin.move(speed="100",add="10")
