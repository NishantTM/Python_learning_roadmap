import os

FILE_NAME = "function/students.txt"

students = []

while True:
    print("Student Management system :")
    print("1. Add Students ")
    print("2. View Students ")
    print("3. Remove Students ")
    print("4. Delete file ")
    print("5. Exit")

    choice = input("Enter the choice (1/2/3/4/5) :")
    # Add student
    if choice == "1":
        try:
            name = input("Enter student name :").strip()

            if not name:
                print("Name can not found ")

            with open(FILE_NAME, "a") as stu:
                stu.write(name + "\n")
            print(f" {name} addedd succesfully :")

        except FileNotFoundError as e:
            print("Error ", e)
        except ValueError as v:
            print("Value not find error ", v)

    # else:
    #     print("Infomation are not valid :")

    # View Students
    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as stu:
                students = [line.strip() for line in stu]
                # students = stu.readlines()

                # print(stu.readlines())

            if not students:
                print("No students found ")

            # if len(students) == 0:
            #     print("No students found ")

            else:
                print("/n Stuent list")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student.strip()}")

        except FileNotFoundError as e:
            print("Studnet file does not exist", e)

    # remove students
    elif choice == "3":
        try:
            with open(FILE_NAME, "r") as stu:
                students = [line.strip() for line in stu]

            if not students:
                print("No students found.")

            else:
                print("\nStudent List:")
                for i, student in enumerate(students, start=1):
                    print(f"{i}. {student}")

                name = input("Enter student name to remove: ").strip()

                if name in students:
                    students.remove(name)

                    with open(FILE_NAME, "w") as file:
                        for student in students:
                            file.write(student + "\n")
                    print(f"{name} removed successfully.")

                else:
                    print("Student not found.")

        except FileNotFoundError:
            print("Student file does not exist.")

        except Exception as e:
            print("Error:", e)

        # with open(FILE_NAME, "w") as stu:
        #     students = [line.strip() for line in stu.readlines()]

        # if not students:
        #     print("No students found ")

        # # else:
        # #     print("File has been successfully removed")

        # print("\nStudent List:")
        # for i, student in enumerate(students, start=1):
        #     print(f"{i}. {student}")

        #     num = int(input("Enter students number to the remove :"))

        #     if num < 1 or num > len(students):
        #         raise ValueError("Invalid student number.")

        #     removed = students.pop(num - 1)

        #     with open(FILE_NAME, "r") as file:
        #         for student in students:
        #             file.write(student + "\n")

        #             print(f"{removed} Removed sucessfully ")

    elif choice == "4":

        try:
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
            else:
                print("File deletd succesfully  ")

        except Exception as e:
            print("Error deleting file:", e)

    elif choice == "5":
        print("Good bye see you next time ")
        break

    else:
        print("Invalid choice try again !")
