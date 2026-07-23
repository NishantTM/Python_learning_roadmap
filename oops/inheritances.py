# # Single level inheritance
# class Vehicle:
#     def start(self):
#         print("Start the Vehicle ")


# class Car(Vehicle):
#     def roar(self):
#         print("Roaring the car")


# c = Car()
# c.start()
# c.roar()


# # Multiple inheritance

# # Multiple inhertiance: Mltileve inhertiance refers to the two parent class and one child class and we can inherit the properties and method from the child class to parent class


# class father:
#     def skills(self):
#         print("Father have Coding knowledge ")


# class Mother:
#     def c_skill(self):
#         print("Mom have cooking knowledge ")


# class Child(father, Mother):
#     def show(self):
#         print("He or she have multiple skills ")


# child = Child()
# child.show()
# child.skills()
# child.c_skill()


# # Multilevel inhertiance
# # In this tupe of inhertance, one parent class and two child class


# class GrandParent:
#     def show_grandP(self):
#         print("I am a grandparent ")


# class Parent(GrandParent):
#     def show_Parent(self):
#         print("I am a parent of child ")


# class Child(Parent):
#     def show_Child(self):
#         print("I am a child")


# child = Child()
# child.show_Child()
# child.show_Parent()
# child.show_grandP()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print("Person Name :", self.name)


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary

#     def display_salary(self):
#         print("Employee Salary :", self.salary)


# class Manaager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display_department(self):
#         print("Department :", self.department)


# manager = Manaager("Nishant", 100000, "IT Department")
# manager.display_department()
# manager.display_salary()
# manager.display_name()



