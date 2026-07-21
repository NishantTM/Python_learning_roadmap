# file = open("file/saple.txt", "a")
# print(file.write("\n  akfjkadfj"))


# file.close()


# with open("student.txt", "w") as file:
#     print(file.write("hello"))

import os

file1 = open("file/hell.txt", "a")
# print(f.read())
# print(f.write("Hey beauty"))
print(file1.write("\n nice to meet you "))


try:
    with open("file/student.txt", "r") as file1:
        # print(file1.write("hello"))
        print(file1.read(300))
        # print(file1.readline())
    # file1.write("\n The student file has more content ")

except FileNotFoundError:
    print("File not found ")


# with open("file/student.txt") as f:
#     print(f.read())

#     os.remove("file/hell.txt")


# if os.path.exists("file/saple.txt"):
#     os.remove("file/saple.txt")

# else:
#     print("The file does not exist :")

# # file1.close()


# Reading an empty file through the exception handling

try:
    with open("file/hello.txt", "r") as f:
        data = f.read()

        if data == "":
            raise Exception("File are empty ")

        print(data)

except FileExistsError as er:
    print("Error: ", er)


try:
    with open("file/firsrrrt.txt", "r") as cr:
        # cr.read("irie hjrhhgejr")
        cr.read()
        print("File created successfully ")

except FileExistsError as e:
    print("Error or file already create ", e)


finally:
    print("The 'try and except' handling succesfully create and read the file ")
