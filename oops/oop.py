"""A class is a blue print"""

# An object is a real thing that is created with the help of blueprint or class.

# class Bag:
#     def __init__(self,brand,zips,pocket):
#         self.brand = brand
#         self.zips = zips
#         self.pocket = pocket


#     def show(self):
#         print(self.brand,self.zips,self.pocket)


# reebbok = Bag("reebook",4,5)
# nike = Bag("nike",2,6)
# nike.show()


class Fruits:
    def __init__(self, name):
        self.name = name


fruts = Fruits("Mango")
print(fruts.name)

# A constructor is a method that is automatically run when object called


class Car:
    name = "tata"

    def __init__(self, brand, price, model):
        self.brand = brand
        self.price = price
        self.model = model

    def display(self, change):
        self.brand = change
        print(self.brand, self.price, self.model, self.name)


car = Car("Nissan", 9000000, "Skyline")
car2 = Car("Toyota Supra", 100000000, "M5")

car.display("dfddf")

print(car.brand)
# car.display()


# Types of methods
# Instance variables
class Vehicle:
    name = "Bike"  # class att

    def __init__(self, brand):
        self.brand = brand  # instance att

    def view(self):  # instance met
        print("Bike Name :", self.brand)
        print("Vehicle :", Vehicle.name)


b1 = Vehicle("hjhedfw")
print(b1.view())


# class methodS
class Student:
    college = "Nesfield Internatinoal college"

    @classmethod
    def change_college(cls, c_name):
        cls.college = c_name

    # def show(cls):
    #     print("Student Name :", cls.name)
    #     print("College Name :", Student.college)


Student.change_college("xavier college")
print(Student.college)


# Static Method


class Car:
    @staticmethod
    def class_method():
        print("Hey hency what are you doing")


Car.class_method()


class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.multiply(5, 10))


# Car.class_method()


# Ineritance
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display_name(self):
        print(self.fname, self.lname)


per = Person("Nishant", "Singh")
print(per.display_name())


# Single level inheritance
class Vehicle:
    def start(self):
        print("Start the Vehicle ")


class Car(Vehicle):
    def roar(self):
        print("Roaring the car")


c = Car()
c.start()
c.roar()


# Encapsulation : Hides a data uring the private variables

# Polymorphism: The same method name behaves differently in different class

# Abstaction: Hides the unneccessay data and only show the necessary data


