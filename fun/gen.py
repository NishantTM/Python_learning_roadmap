# # return
# def students():
#     return ["Ram", "Shyam", "Mohan"]

# for name in  students():
#     print(name)

# # yield
# def student1():
#     yield "nishant"
#     yield "Rohan"
#     yield "sujan"


# for name in students():
#     print(name)

# generatlr expressions

list_comp = [x * x for x in range(5)]
print(list_comp)


gen_xp = (x * x for x in range(5))
# print(gen_xp)
print(list(gen_xp))


total = sum(x * x for x in range(10))
print(total)



tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Furits")
    print("2. View Furits")
    print("3. Remove Furit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add task
    if choice == "1":
        task = input("Enter Furits name : ")
        tasks.append(task)
        # append = add
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No Furits available.")

        else:
            print("\nYour Furits:")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No Furits to remove.")
        else:
            num = int(input("Enter Fruits number to remove: "))
            if num >= 1 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid Furits number!")

    # Exit
    elif choice == "4":
        print("Thank you! Goodbye")
        break

    else:
        print("Invalid choice! Try again.")
