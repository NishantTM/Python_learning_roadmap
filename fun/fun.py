# # # a = 4
# # # b = 5
# # # print(a + b)


# # # r = 5
# # # s = 6
# # # print()


# # # def add(a,b):
# # #     print(a + b)


# # # add(2,4)
# # # add(4,5)


# # # def greet(name):
# # #     print( name)


# # # greet("ram")


# # # def order(*momo):
# # #     print(momo)

# # # order(1,2,4,5,6)


# # # # local variable
# # # def my_func():
# # #     x = 500
# # #     print(x)


# # # my_func()

# # # # global variable
# # # y = 5000


# # # def my_func():
# # #     print(y)


# # # my_func()
# # # print(y)

# # # # y = 7
# # # def add():
# # #     x = 4
# # #     print(x)
# # #     print(y)


# # # add()

# # # print(y)

# # # global keyword
# # # x = 2000000


# # # def fun_1():
# # #     global x
# # #     x = 100


# # # fun_1()
# # # print(x)


# # # # python decorators
# # # def change(func):
# # #     def myInner():
# # #         return func().lower()

# # #     return myInner


# # # @change
# # # def my_function():
# # #     return "Hellow guys"


# # # print(my_function())


# # # Multiple decoratos call
# # def changecase(func):
# #     def myInner():
# #         return func().upper()

# #     return myInner


# # @changecase
# # def my_function1():
# #     return "Say No"


# # @changecase
# # def my_function2():
# #     return "Say Yes and what are you doing"


# # print(my_function1())
# # print(my_function2())

# # # Lambda functions

# # # x = lambda a : a + 10
# # # print(x(5))


# # # x = lambda a, b: a * b
# # # print(x(9,10))

# # # x = lambda a, b, c: a * b * c
# # # print(x(3,4,5))


# # # def myfunc(n):
# # #     return lambda a: a * n


# # # mydoubler = myfunc(3)
# # # print(mydoubler(9))


# # # def myfunc1(n):
# # #     return lambda a: a * n


# # # mydoubler = myfunc1(4)
# # # mytipler = myfunc1(10)

# # # print(mydoubler(9))
# # # print(mytipler(9))


# # # # Lambda with the built in functions
# # # number =

# # # students = [("Ram", 85), ("Shyam", 70), ("Hari", 90)]

# # # result = sorted(students, key=lambda x: x[1])

# # # print(result)


# # # name = input("Enter student Name :")
# # # marks = int(input("Enter the marks of the subject : "))
# # # # grade = input("Enter your grade: ")

# # # grade = ""

# # # # for i in range(90, 100):
# # # for i in range(5):
# # #     if i > (90, 100):
# # #         print("Enter the marks of the subject : ", marks)
# # #         print("The student marks is", {i + 1})
# # #         grade = "A+"

# # # # for i in range(80, 90):
# # # #     if i == marks:
# # # #         grade = "A"

# # # # for i in range(70, 80):
# # # #     if i == marks:
# # # #         grade = "B+"

# # # # for i in range(60, 70):
# # # #     if i == marks:
# # # #         grade = "B"

# # # # for i in range(50, 60):
# # # #     if i == marks:
# # # #         grade = "C+"

# # # print("\n ---Student Result -----")
# # # print("Name: ", name)
# # # print("Marks: ", marks)
# # # # print("Subject: ", )
# # # print("Grade :", grade)


# # def grade(marks):
# #     if marks >= 90 and marks <= 100:
# #         print("A+")

# #     elif marks >= 80 and marks < 90:
# #         print("A")

# #     elif marks >= 70 and marks < 80:
# #         print("B+")

# #     elif marks >= 60 and marks < 70:
# #         print("B")

# #     elif marks >= 50 and marks < 60:
# #         print("C+")

# #     elif marks >= 40 and marks < 50:
# #         print("D+")

# #     elif marks >= 30 and marks < 40:
# #         print("D")

# #     elif marks >= 20 and marks < 30:
# #         print("NG")

# #     else:
# #         print("Invalid Marks")


# # for sub in range(5):
# #     marks = int(input(f"Enter marks for subject {sub + 1}: "))
# #     print("Marks:", marks)
# #     print("Grade:", end=" ")
# #     grade(marks)


# #  Calculator


# def calculator_1():

#     print("Select an Operation :")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4 Division")

#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter Second number: "))
#     choice = int(input("Enter your choice: (1/2/3/4) "))

#     if choice == 1:
#         print(f"Addition : {num1} + {num2} = {num1 + num2} ")

#     elif choice == 2:
#         print(f" Subtraction: {num1} - {num2} = {num1 - num2} ")

#     elif choice == 3:
#         print(f" Multiplication: {num1} * {num2} = {num1 * num2} ")

#     elif choice == 4:
#         print(f" Division: {num1} / {num2} = {num1 / num2} ")

#     else:
#         print("Invalid Opertation :")


# calculator_1()


# # ATM System
# def atm_system():
#     correct_pin = 1234
#     balance = 20000

#     pin = int(input("Enter pin:"))

#     if pin != 1234:
#         print("Invalid pin")
#         return

#     print("-----Login successful ------")

#     while True:
#         print("ATM MENU")
#         print("1. Check Balance ")
#         print("2. Fast cash")
#         print("3. Withdraw amount")
#         print("4. Deposit amount")

#         choice = int(input("Enter your choice:"))

#         if choice == 1:
#             print(f"The balance are {balance}")

#         elif choice == 2:
#             print("\Fast Cash")

#         option = int(input("Choose amount :"))

#         if option == 1:
#             amount = 500

#         elif option == 2:
#             amount = 1000

#         elif option == 3:
#             amount = 2000

#         elif option == 4:
#             amount = 5000

#         else:
#             print("Invalid amount ")

#         if amount <= balance:
#             balance -= amount

#             print(f" Please collect your cash {amount}")
#             print(f" Remaining balance are {balance}")

#         else:
#             print("Insuffieient balance")

#         # elif choice == 3:

# atm_system()

# def atm_sy():
#     int(input("Enter pin :"))
#     print("Select a service ")
#     print("1. Fast cash ")
#     print("2. Withdraw amount ")


#     num1 = int(input("Your are succesfully withdraw an amount from your account "))
#     num2 = int(input("You ca withdraw an such amount "))

#     choice = int(input("Enter your choice: 1/2"))

#     if choice == 1:
#         print(f"Withdraw amount are : {num1} + {num2} = {num1, num2}")

#     if choice == 2:
#         print(f"Withdraw amount are : {num1} - {num2} = {num1, num2}")


# atm_sy()


# Student Grade System
# Student Record Management
# Library Management
# # Employee Management
# # Hotel Billing System
# # Restaurant Billing System
# # Quiz Game
# # Number Guessing Game
# # Password Generator
# # Contact Book
# # Voting System
# # Bank Account Management
# # Inventory Management System


# # TO DO list
# tasks = []

# while True:
#     print("---TO DO LIST----")
#     print("1. Added fruits :")
#     print("2. View  fruits :")
#     print("3. Remove fruits :")
#     print("4. Exit App :")

#     choice = input("Enter your choice from (1-4): ")

#     # Add

#     if choice == "1":
#         task = input("Enter your task or fruit :")
#         tasks.append(task)
#         print("Task or fruit added succesfully :")

#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No fruits available ")

#         else:
#             print("Your fruits ")
#             for i in range(len(tasks)):
#                 print(f"{i+1}.{tasks[i]}")

#     elif choice == "3":
#         if len(tasks) == 0:
#             print("No fruits to remove ")
#         else:
#             print("\nYour Fruits:")
#             for i in range(len(tasks)):
#                 print(f"{i+1}.{tasks[i]}")

#             num = int(input("Enter a fruits to remove "))

#             if 1 <= num <= len(tasks):
#                 removed = tasks.pop(num - 1)
#                 print(f" Removed task :{removed}")

#             else:
#                 print("Invalid fruits")

#     elif choice == "4":
#         print("Good bye")
#         break

#     else:
#         print("Invalid choice try again !")

# student managmemet system

students = []
while True:
    print("Student Management system :")
    print("1. Add Students ")
    print("2. View Students ")
    print("3. Remove Students ")
    print("4. Exit")

    choice = input("Enter the choice (1/2/3/4) :")

    if choice == "1":
        name = input("Enter student name :")
        students.append(name)
        print("Student addedd succesfully :")

    # else:
    #     print("Infomation are not valid :")

    elif choice == "2":
        if len(students) == 0:
            print("No students found ")

        else:
            print("/n Stuent list")
            for i in range(len(students)):
                print(f"{i + 1}. {students[i]}")

    elif choice == "3":
        if len(students) == 0:
            print("No students found ")
        else:
            for i in range(len(students)):

                print(f"{i + 1}. {students[i]}")

            num = int(input("Enter students name for the remove :"))

        if num >= 1 and num <= len(students):
            removed = students.pop(num - 1)
            print(f"{removed} Removed sucessfully ")

    elif choice == "4":
        print("Good bye")
        break

    else:
        print("Invalid choice try again !")
