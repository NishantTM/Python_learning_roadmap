# # The try blocks lets you test a block of code of errors
# # The except blocks lets you handle the error
# # The else blocks lets you execute when there is no error
# # The finally blocks lets you execute the code, regardless of the result of the try-and except blocks

# # try block
# try:
#     print(x)
# except:
#     print("An exception occured")


# # Try example
# try:
#     num = int(input("Enter a number :"))
#     print("You entered ", num)

# except:
#     print("Something error :")
# try:
#     print(x)
# except:
#     print("Something error: ")
# finally:
#     print("The 'try' are finished ")

# # exception block
# try:
#     a = 10
#     b = 50
#     print(a / b)

# except:
#     print("Can not divide by the zero ")


# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age :"))

# except ValueError:
#     print("Age must be a number :")

# else:
#     print("Welcome ", name)
#     print("Age ", age)

# finally:
#     print("Thank you and goodbyw")


def grade(marks):

    try:
        if marks < 20 or marks >= 100:
            raise ValueError("Marks between 20 to 100")

        if marks >= 90 and marks <= 100:
            print("A+")

        elif marks >= 80 and marks < 90:
            print("A")

        elif marks >= 70 and marks < 80:
            print("B+")

        elif marks >= 60 and marks < 70:
            print("B")

        elif marks >= 50 and marks < 60:
            print("C+")

        elif marks >= 40 and marks < 50:
            print("D+")

        elif marks >= 30 and marks < 40:
            print("D")

        elif marks >= 20 and marks < 30:
            print("NG")

        # except:
        # print("Enter valid marks ")
    except ValueError as e:
        print("Error :", e)

        # print("Something error! enter a valid marks ")

    # else:
    #     print("Invalid Marks")

    finally:
        print("The grade of students are calculated :")


for sub in range(5):
    marks = int(input(f"Enter marks for subject {sub + 1}: "))
    print("Marks:", marks)
    print("Grade:", end=" ")
    grade(marks)
