# '''
# Till now we were using procedural programming and now we will use OOp
# It uses Classes and Objects
# CLASS:-
#
# Class is a template for creating objects
# It defines properties(Data of object)and methods(Actions an object can perform...)
#
# CLASSES AND OBJECTS
# '''
#
# class Person:
#     name ="AbMohiz"
#     occupation ="Programmer"
#     age = 20
#     networth = 10000
#     def info(self):
#         print(f"Name is: {self.name}\n occupation is:{self.occupation}\n Age is:{self.age}\n {self.networth}")
#
#
# # Object 1
# a = Person()
# # Making the 2nd object
# b = Person()
# b.name = "Zohaib"
# b.occupation = "Graphic Designer"
# b.age = 23
#
# # if you want to change the name:   print(a.name, a.age)
# # a.name = "Zohaib"
# # a.occupation = "Zohaib"
# #Calling self function first time
# print(a.info())
# print(b.info())
#
# # b = Person()
# #     name ="AbMohiz"
# #     occupation ="Programmer"
# #     age = 20
# #     networth = 10000
#
# '''
# Now we will Use Constructor:
#
# Special method in a class used to create and initialize an object of classes
# It Always return None
#
# '''
# class Cars:
#     model = "Ford"
#     year = 1999
#     country = "ENG"
#
#     ''' C O N S T R U C T O R '''
#     def __init__(self,model,year,country):
#         print("CARS DETAILS ARE FOLLOWING:")
#         self.model = model
#         self.year = year
#         self.country = country
#
#
#     '''Default CONSTRUCTOR'''
#
#     # def __init__(self):
#     #         print("CARS DETAILS ARE FOLLOWING:")
#
#     def info1(self):
#         print(f"The car name is {self.model}\nyear is: {self.year}\nIn country:{self.country} ")
#
# d = Cars("Honda",2000,"Japan")
# g = Cars("Toyota ",1999,"Japan")
# # d = Cars()
# d.info1()
# g.info1()
# # print(Cars.model)

class Vehicle:
    maxspeed = 120
    milage = 200000

    def veh(self):
        print(f"Vehicle max speed is :{self.maxspeed} and milage is :{self.milage}")

a = Vehicle()
print(a)
a.veh()
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed,modelX.mileage)

