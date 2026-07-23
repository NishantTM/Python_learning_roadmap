# Question 1: Student

# Create a Student class.

# Requirements:

# name
# age
# faculty

# Methods:

# display()


class Student:
    def __init__(self, name, age, faculty):
        self.name = name
        self.age = age
        self.faculty = faculty

    def display(self):
        print("Name:", self.name)
        print("Age :", self.age)
        print("Faculty :", self.faculty)


student1 = Student("Karan", 30, "BBM")
student2 = Student("Arjun", 32, "BCA")

student1.display()
# student2.display()

# Question 2: Book

# Create a Book class.

# Attributes:

# title
# author
# price

# Methods:


# display()
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)


bk = Book("RED ROSE", "JKRowling", 100000)

bk.display()


# Level 2: Instance Methods
# Question 4: String Manager

# Methods:

# uppercase()
# lowercase()
# reverse()
# count_vowels()


class String_Manager:
    constant = "In the price"

    def __init__(self, constant):
        self.constant = constant

    def uppercase(self):
        print(self.constant.upper())

    def lowercase(self):
        print(self.constant.lower())

    def reverse(self):
        print(self.constant[::-1])

    def count_vowels(self):
        count = 0

        for ch in self.constant.lower():
            if ch in "aeiou":
                count += 1

        print("Total Vowels", count)


sm = String_Manager("hey dhilo what happening hiiiiii hfijsdhfi ")
sm.uppercase()
sm.lowercase()
sm.reverse()
sm.count_vowels()

# sm.count_vowels()


# Level 3: Class Variables
# Question 7

# Create a Student class.

# Every student belongs to the same college.

# College = "Nesfield International College"

# Display the college name for every object.


class Student:
    college = "Nesfield internation college"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("College Name :", Student.college)


stu = Student("Nishant", 22)
stu1 = Student("ishwor", 23)

# stu2 = Student(college="Nesfield internation college")

stu.display()
stu1.display()


# Practice Challenge

# Create an Employee class.

# Requirements:

# Class variable:

# company = "OpenAI"
# Instance variables:
# name
# salary

# display() should print:

# Name: Nishant
# Salary: 50000
# Company: OpenAI


class Employee:
    company = "Open AI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display1(self):
        print("Name ", self.name)
        print("Salary ", self.salary)
        print("Company Name :", Employee.company)


emp = Employee("Herbel", 900000)
emp2 = Employee("John Wicki", 1200000)

emp.display1()
emp2.display1()
