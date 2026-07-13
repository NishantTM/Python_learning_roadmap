# ---------------------- Python List---------------------------




# # Definition:
# # A list is an ordered collection of items that is mutable (can be changed) and allows duplicate values.


#a = [1,2,2,2,2,3,4,6,]
#print(a)

#name = ["ram","hari","shyam","radhat","sita"]

# # Why use:
# # Store multiple items in a single variable
# # Keep items in order (indexing possible)
# # Perform operations like add, remove, search, sort
# # Useful for shopping lists, student names, task lists, sensor data, etc.

# # Syntax:
# # my_list = [item1, item2, item3]



# fruits = ['apple', 'bananna','mango','oranage']
# numbers = [1,2,3,3,4,"banana",3.5]

# # Access List Item----------
# # Definition: Retrieve item from list using index
# # Why use: To get specific data



	
# fruits = ["apple", "banana", "mango"]
# print(fruits[0])   # apple
# print(fruits[-1])  # mango



# # # # Real-world: Get first student from list, last product in cart




# # Change List Item-------------

# # Definition: Modify item at a specific index
# # Why use: Update values
# fruits = ["apple", "banana", "mango"]
# fruits[1] = "orange"
# print(fruits) 


#['apple', 'orange', 'mango']
# # Real-world: Change task status, update price


# # Add List Item------------

# # Methods:
# # Definition: Add new items to list
# # append() → add at end
# # insert() → add at specific index
# # extend() → add another list


# fruits = ["apple", "banana", "mango"]

# # a = ["apple", "banana", "mango"]

# fruits.append("grape")
# print(fruits)
# fruits.insert(1, "kiwi")
# fruits.extend(["pineapple", "watermelon"])
# print(fruits)

# # Real-world: Add new product to inventory, add new student


# # Remove List Item-----------




# # Definition: Delete item from list
# # remove(value) → by value
# # pop(index) → by index
# # del list[index] → delete index
# # clear() → remove all items


# fruits = ["apple", "banana", "mango"]
# fruits.remove("kiwi")
# fruits.pop(0)
# del fruits[1]
# fruits.clear()


# # Real-world: Remove sold product, remove completed task

# # Loop Lists--------------



# # Definition: Iterate through list items
# # Why use: Perform actions on each item
# #  (for loop):


# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)
    
# # # (while loop)
# # i = 0
# # while i < len(fruits):
# #     print(fruits[i])
# #     i += 1
# # Real-world: Print all student names, process all orders

# # List Comprehension----------------



# # Definition: Quick way to create lists using one line
# # Why use: Shorter code, efficient

# squares = [x**2 
#         for x in range(1,6)]
# print(squares)  # [1, 4, 9, 16, 25]
# # Real-world: Generate square of numbers, filter even number


# # Sort List---------------


# # Definition: Arrange items in order
# # Methods:
# # sort() → ascending
# # sort(reverse=True) → descending
# # sorted(list) → return new sorted list

# numbers = [5, 2, 9, 1]
# numbers.sort()
# print(numbers)  # [1,2,5,9]
# numbers.sort(reverse=True)
# print(numbers)  # [9,5,2,1]

# fruits = ["apple", "canana", "bango"]
# # fruits.sort()

# # for i in fruits:
# #         print(i)
        
# fruits.sort(reverse=True)
# for j in fruits:
#         print(j)


# # Real-world: Sort students by marks, products by price

# # Copy List-----------------
# # Definition: Create duplicate of list
# # Why use: Avoid changing original list
# # Methods: copy() or list()

# fruits = ["apple", "canana", "bango"]
# fruits_copy = fruits.copy()
# fruits_copy2 = list(fruits)
# print(fruits)
# print(fruits_copy2)

# # Real-world: Backup student list before update

# #  Join List------------
# # Definition: Combine two or more lists
# # Methods:
# # + operator → concatenate
# # extend() → add another list

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = list1 + list2



# list1.extend(list2)
# print(list3)   # [1,2,3,4,5,6]
# print(list1)   # [1,2,3,4,5,6]

# # Real-world: Combine order lists, merge datasets

# # List Methods---------


# # Method	Description
# # append()	Add item at end
# # insert()	Add item at specific index
# # extend()	Add multiple items
# # remove()	Remove by value
# # pop()	Remove by index
# # clear()	Remove all items
# # sort()	Sort ascending
# # reverse()	Reverse list
# # index()	Find index of item
# # count()	Count occurrences
# # copy()	Copy list


# # List Exercises----------
# # 1.	Create a list of 5 favorite fruits and print it
# # 2.	Change the second item to "orange"
# # 3.	Add a new fruit at the end
# # 4.	Remove the first fruit
# 5.	Print all fruits using for loop
# # 7.	Sort the list [5,2,9,1] ascending and descending
# # 8.	Join two lists [1,2,3] and [4,5,6]


# # Tips ------------
# # Lists are mutable, ordered, allow duplicates
# # Indexing starts from 0
# # Commonly used methods → append, insert, remove, pop, sort, extend
# # List comprehension 


# # append()--------------
# # Definition: Add item at the end of the list
# # Why use: To add new element to a list without changing existing items

# fruits = ["apple", "banana"]
# fruits.append("mango")
# print(fruits)
# ['apple', 'banana', 'mango']

# # Use case: Add new product to inventory, add new student to class list

# # insert()--------------
# # Definition: Add item at a specific index
# # Why use: To insert element at exact position
# # Syntax: list.insert(index, item)

# fruits = ["apple", "banana"]
# fruits.insert(1, "orange")
# print(fruits)

# ['apple', 'orange', 'banana']


# # Use case: Add new task in specific position in todo list

# # extend()------------
# # Definition: Add multiple items from another list
# # Why use: Combine lists or add multiple items at once

# fruits = ["apple", "banana"]
# fruits.extend(["mango", "grape"])
# print(fruits)

# ['apple', 'banana', 'mango', 'grape']
# # Use case: Merge two datasets, add multiple products to inventory

# # remove()------------
# # Definition: Remove first occurrence of a value
# # Why use: To delete specific item from list

# fruits = ["apple", "banana", "mango"]
# fruits.remove("banana")
# print(fruits)

# # ['apple', 'mango']
# # Use case: Remove sold item, remove task from todo list

# # pop()----------
# # Definition: Remove item at a specific index (default last) and return it
# # Why use: Remove and optionally use the removed value

# fruits = ["apple", "banana", "mango"]
# item = fruits.pop(1)
# print(item)    # banana
# print(fruits)  # ['apple', 'mango']

# # Use case: Remove last order from cart, remove student from class

# # clear()---------------
# # Definition: Remove all items from list
# # Why use: Empty list completely

# fruits = ["apple", "banana", "mango"]
# fruits.clear()
# print(fruits)
# # []
# # Use case: Reset shopping cart, clear old data

# # sort()------------
# # Definition: Sort items in ascending order by default
# # Why use: Organize data for easy search and display

# numbers = [5, 2, 9, 1]
# numbers.sort()
# print(numbers)


# # [1, 2, 5, 9]
# # Use case: Sort student marks, product prices

# # reverse()-----------------
# # Definition: Reverse the order of list items
# # Why use: To display list in reverse order

# numbers = [1,2,3,4]
# numbers.reverse()
# print(numbers)

# # [4,3,2,1]
# # Use case: Display latest entries first

# # index()---------------
# # Definition: Find the index of first occurrence of a value
# # Why use: To know position of an item in list

# fruits = ["apple", "banana", "mango"]
# print(fruits.index("banana"))

# # 1
# # Use case: Find student roll number, product position in list



# # count()-----------------
# # Definition: Count occurrences of a value in list
# # Why use: To see how many times an item appears

# numbers = [1,2,2,3,2]
# print(numbers.count(2))

# # 3
# # Use case: Count repeated orders, repeated tasks



# # copy()--------------------
# # Definition: Return a shallow copy of list
# # Why use: Work on duplicate list without changing original

# fruits = ["apple", "banana"]
# fruits_copy = fruits.copy()



# fruits_copy.append("mango")




	
# print(fruits)       # ['apple', 'banana']
# print(fruits_copy)  # ['apple', 'banana', 'mango']
# # Use case: Backup student list, backup dataset

# # Tips -----------
# # Remember: append, insert, extend → adding items
# # remove, pop, clear → deleting items
# # sort, reverse → arranging items
# # index, count → finding information
# # copy → duplicate without changing original


# print(" list of name ")
# name = ['ram','hari','shyam','sita','gita']
# print(name)

# print('check for specific item in the list ')
# checkitem = input('Enter an item to for check :')

# # for i in name:
# #         if i == checkitem:
# #                 print('item found in the item ')
# #                 break
# # else:
# #         print('item not found in the list')


# if checkitem in name :
#         print("found")
# else:
#         print('not found')


# # shallow copy creates a new object but references the same nested objects, so changes to nested objects affect both original and copy.
# import copy

# student_data = [
#     {"name": "Ram", "marks": [80, 90]},
#     {"name": "Sita", "marks": [85, 95]}
# ]

# test_data = copy.deepcopy(student_data)

# # Update marks in test_data
# test_data[0]["marks"][0] = 100

# print(student_data)
# print(test_data)





# # Deep copy creates a new object and recursively copies all nested objects, ensuring that changes to the copy do not affect the original.


# import copy

# # Original nested data
# students = [
#     {"name": "Ram", "marks": [80, 90]},
#     {"name": "Sita", "marks": [85, 95]}
# ]

# # Deep copy
# students_copy = copy.deepcopy(students)

# # Change marks in the copy
# students_copy[0]["marks"][0] = 100

# # Print both to see difference
# print("Original:", students)
# print("Copy    :", students_copy)


# 1. Create a list of 5 numbers and print it.
# 2. Create a list of 5 student names and print it.
# 3. Print the first element of a list.
# 4. Print the last element of a list.
# 5. Add a new element to the end of a list.
# 6. Insert a new element at index 2 in a list.
# 7. Remove an element from a list using remove().
# 8. Remove the last element using pop().
# 9. Find the length of a list.
# 10. Sort a list of numbers in ascending order.
# 11. Sort a list of numbers in descending order.
# 12. Reverse a list.
# 13. Check if a specific item exists in a list.
# 14. Count how many times a number appears in a list.
# 15. Create an empty list and add 3 elements to it.