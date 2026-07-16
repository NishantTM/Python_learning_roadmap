import copy

# # # name = "ram"
# # # age = 12
# # # marks = int(12.2)

# # # age1 = "3"

# # # c = float(age1)

# # # print(type(name))
# # # print(type(age))
# # # print(type(c))


# # # name = "hari ram"
# # # print(name[3:6])


# # # name = "hell0"
# # # # print(name[0 : 5 : 2])

# # # # hey = "how-are-you guys"
# # # # print(hey[2:10 : 3])

# # # # h1 = "yau whatsapp guyswhat are you doing"
# # # # print(h1[2: : 6])

# # # print(name[-2 : ])

# # # age =  22
# # # name = "ram"
# # # print(f'age {age} name {name}' )

# # #  modify string
# # # a = "Hellow, world"
# # # print(a.upper())
# # # print(a.lower())

# # # # Remove whitespace
# # # a = " Hello, World! "
# # # print(a.strip())


# # # b = "Hey how are you guys!"
# # # print(b.replace("H", "Y"))

# # # # format strings
# # # price = 59
# # # txt = f"The price is {price} dollars"
# # # print(txt)

# # # # Display the price with 2 decimals:

# # # price = 60
# # # tx1 = f"The price of {price:.2f} dollars"
# # # print(tx1)


# # # captialize functions
# # h1 = "Hello guys how ARE  You"
# # x = h1.capitalize()
# # print(x)

# # # center function
# # txt1 = "Apple"
# # x1 = txt1.center(10,"_")
# # print(x1)


# # # count functions
# # txt3 = "Hey my favourite fruit is apple, i eat apple in my daily life and routine"
# # x3 = txt3.count("i")
# # print(x3)

# # # Lower and upper  functions
# # txt4 = "Hey guys welcome to my python course"
# # x4 = txt4.upper()
# # print(x4)

# # # is upper functions
# # txt4 = "Hey guys welcome to my python course"
# # x4 = txt4.isupper()
# # print(x4)

# # # split functions
# # txt5 = "Welcome to the my python learning course"
# # x5 = txt5.split()
# # print(x5)

# # # starts with functions
# # txt6 = "hwt guys how are you."
# # x6 = txt6.startswith("v")
# # print(x6)


# # # strip functions
# # txt7 = "         hhhhhhh       "
# # x7 = txt7.strip()
# # print(x7)


# # # swap case functions
# # txt8 = "Hey wow How are you"
# # x8 = txt8.swapcase()
# # print(x8)

# # # Zfill method or functios
# # txt9 = "1000"
# # x9 = txt9.zfill(20)
# # print(x9)

# # # title functions
# # txt10 = "Hwlo guys hihih fuweh wffdhbhbdh"
# # x10 = txt10.title()
# # print(x10)


# # a = 4
# # b = 6

# # c = a

# # print(id(a))
# # print(id(b))
# # print(id(c))


# # print(a is c)

# marks = 25

# if marks >= 90 and marks <= 100:
#     print("A+")

# elif marks >= 80 and marks < 90:
#     print("A")

# elif marks >= 70 and marks < 80:
#     print("B+")

# elif marks >= 60 and marks < 70:
#     print("B")

# elif marks >= 50 and marks < 60:
#     print("C+")

# elif marks >= 40 and marks < 50:
#     print("D+")

# elif marks >= 30 and marks < 40:
#     print("D")

# elif marks >= 20 and marks < 30:
#     print("NG")


# # Nested if
# age = 25
# has_license = False

# if age >= 18:
#     if has_license:
#         print("You can drive")
#     else:
#         print("You need a license")
# else:
#     print("You are too young to drive")

# # pass statement
# a = 60
# b = 40
# if b > a:
#     pass

# else:
#     print("b is greater than a")

# #   match statement
# # day = 6
# # match day:
# #    case 1:
# #       print("Sunday")
# #     case 2:
# #             print("Monday")
# #       case 3:
# #              print("Tuesday")


# # print odd or even using if else
# def ODD_EVEN(num):
#     if num % 2 == 0:
#         print("Even number")

#     else:
#         print("ODD number")


# ODD_EVEN(7)


# # display the celcious and human body of the temperature


# def check_termerature(temp):
#     print("Temperature: ", temp, "C")

#     if temp == 37:
#         print("The temperature is Normal")
#     elif temp > 37:
#         print("The temperature is high")

#     else:
#         print("Temperature is low")


# check_termerature(37)


# # print the three greatest numbers


# def greatest(n1, n2, n3):
#     if n1 >= n2 and n1 >= n3:
#         print("Greatest number:", n1)
#     elif n2 >= n1 and n2 >= n3:
#         print("Greatest number:", n2)
#     else:
#         print("Greatest number:", n3)


# greatest(500, 6, 8)


# # match statment
# day = 4
# match day:

#     case 1:
#         print("Sunday")

#     case 2:
#         print("Monday")

#     case 3:
#         print("Tuesday")

#     case 4:
#         print("Wednesday")

#     case 5:
#         print("Thursday")

#     case 6:
#         print("Friday")

#     case 6:
#         print("Saturday")

names = ["ram", "shyam", "hari"]


name = ["ram", "shyam", "hari"]
# name[0] = "Sita"
# name.append("sota")
# name.insert(2,"janaki")
# name.extend(names)
# name.remove("ram")
# name.pop(2)
# del name[1]
# name.clear()
print(name)


# arrange by items
numbers = [1, 2, 3, 14, 5, 7, 9]
# numbers.sort()
numbers.sort(reverse=True)

print(numbers)


fruits = ["Apple", "Banana", "Mango"]
# fruits.sort()
fruits.sort(reverse=True)
for j in fruits:
    print(j)

# print(fruits)


# copy list

fruits = ["Apple", "Banana", "Mango"]
fruit_copy = fruits.copy()
fruits_copy2 = list(fruits)
print(fruit_copy)
print(fruits_copy2)

# slice operator
this_list = ["Hey", "Hello", "Hi", "Hoe"]
my_list = this_list[:]
print(len(my_list))

# #  Join List------------

list1 = [1, 2, 4, 6]
list2 = ["a", "b", "d"]

# list3 = list1 + list2
# print(list3)
# append method
for i in list2:
    list1.append(i)

    print(list1)


# extend method
list1.extend(list2)
print(list1)


# Create a list called colors with the values "red", "green", "blue"
# Print the first item in the list
# Change the second item to "yellow"
# Add "purple" to the end of the list using append()
# Remove "red" from the list using remove()
# Print the list


colors = ["red", "green", "blue"]
print(colors[0])

colors[1] = "Yellow"
print(colors)

colors.append("purple")
print(colors)

colors.remove("red")
print(colors)

fruits = ["apple", "mango", "banana", "Orange", "Guava"]
fruits[1] = "Orange"
fruits.append("pineappple")

for i in fruits:
    print(fruits)


list = [5, 2, 9, 1]
# list.sort()
list.sort(reverse=True)
print(list)

fruits.extend("grapes")
print(fruits.count("Orange"))


items = fruits.pop(1)
print(items)


# # Original nested data
students = [
    {"name": "Ram", "roll_no": 14, "marks": [80, 90]},
    {"name": "Sita", "roll_no": 18, "marks": [85, 95]},
]

test_data = copy.deepcopy(students)

test_data[0]["marks"][0] = 100
print(students)
print(test_data)


# Create an empty list and add elements dynamically
# Take 5 inputs from user and store in a list
# Print only even numbers from a list
# Print only odd numbers from a list
# Find the sum of all elements
# Find the maximum value
# Find the minimum value
# Replace an element with a new value
# Remove duplicate elements
# Print elements greater than a given number


# Create an empty list and add elements dynamically
# Take 5 inputs from user and store in a list
numbers = []

for i in range(5):
    num = int(input("Enter a numbers :"))
    numbers.append(num)

# Print only even numbers from a list
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 == 0:
        print("Even numbers")

# Print only ODD numbers from a list
numbers = [2, 4, 6, 8, 10, 15, 13, 17]
for num in numbers:
    if num % 2 != 0:
        print("Odd numbers")


# numbers = [2, 4, 6, 8, 10]
# if numbers % 2 == 0:
#     print("Odd numbers")

total = 0

for i in range(1, 10):
    total += i

    print("Sum  elements are :", total)


list2 = [2, 4, 6, 9, 19, 45]

for i in list2:
    max(list2)

print(i)


list2 = [2, 4, 6, 9, 19, 45]

minimum = min(list2)
print(minimum)

# Replace an element with a new value
numb = [12, 45, 60, 90]
numb[3] = 300
print(numb)


# Remove duplicate elements

# num = [2, 4, 5, 6, 7, 7, 8, 8, 8]
# for i in num:
#     list(set(num))

# print(i)

# Print elements greater than a given number
numbers = [10, 20, 30, 40, 50, 5, 7, 9]

limit = int(input("Enter limit: "))

for num in numbers:
    if num > limit:
        print(num)
