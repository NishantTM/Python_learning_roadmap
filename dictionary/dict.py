# # # ================================================
# # # PYTHON DICTIONARIES – COMPLETE NOTES
# # # ================================================

# # # DEFINITION:
# # # A dictionary is an unordered and mutable collection of key:value pairs in Python.
# # # - Keys must be unique
# # # - Values can be of any data type

# # # WHY USE DICTIONARIES:
# # # • Store data in key-value format
# # # # • Fast lookup using keys
# # # # • Useful for student records, phonebooks, user profiles, configurations


# # # student = {
# # # "name":"ram",
# # # "age": 21,
# # # "address": "ktm"
# # # }
# # # print(student)

# student = {"name": "ram", "age": 21, "address": "ktm"}
# print(student)

# # # SYNTAX:
# # # my_dict = {"key1": value1, "key2": value2}

# # # ------------------------------------------------
# # # 1. ACCESS ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Retrieve value from a dictionary using a key.

# # # Why use:
# # # To access specific data.

# # # Example:

# student = {
#     "name": "ram",
#     "age": 22,
#     "age": 22,
#     "city": "Kathmandu",
# }


# print(student["grde"])
# print(student.get("grade"))  # None

# for key in student:
#     print(key)


# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(f"{key}: {value}")

# # # Sandeep

# # # print(student.get("age"))  # 22

# # # --------------------------------
# # # Example 1: Normal get()
# # # --------------------------------
# # # print(student.get("age"))    # 22
# # # print(student.get("name"))   # Sandeep

# # # Explanation:
# # # • "age" key exists → returns value 22
# # # • "name" key exists → returns value "Sandeep"

# # # --------------------------------
# # # Example 2: Key not present
# # # # --------------------------------
# # # print(student.get("grade"))  # None

# # # Explanation:
# # # • "grade" key does not exist
# # # • No error occurs, returns None

# # # --------------------------------
# # # Example 3: Key not present with default value
# # # --------------------------------
# # # print(student.get("grade", "Not Assigned"))  # Not Assigned

# # # Explanation:
# # # • Key not found → default value is returned

# # # --------------------------------
# # # Why get() is better than dict[key]
# # # --------------------------------
# # # # Using [] → Error if key is missing
# # # # print(student["grade"])   # KeyError

# # # # Using get() → Safe
# # # print(student.get("grade")) # None (no error)

# # # Use cases:
# # # • Student database → get marks safely
# # # • Configuration files → access optional settings safely

# # # Real-world examples:
# # # • Get student's age
# # # • Get product price

# # # ------------------------------------------------
# # # 2. CHANGE ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Update the value of an existing key.

# # # Example:
# # # student={'name': 'Sandeep', 'age': 22, 'city': 'Kathmandu'}
# # # student["age"] = 23
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu'}

# # # Real-world use:
# # # • Update student marks
# # # • Update product price

# # # ------------------------------------------------
# # # 3. ADD ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Add a new key-value pair to the dictionary.

# # # Example:
# # # student["grade"] = "A"
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu', 'grade': 'A'}

# # # Real-world use:
# # # • Add new student information
# # # • Add new product details

# # # ------------------------------------------------
# # # 4. REMOVE ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Removing key:value pairs from a dictionary.

# # # Why use:
# # # • Remove outdated data
# # # • Remove incorrect entries
# # # • Clean database or configuration data

# # # --------------------------------
# # # 1. pop(key)
# # # --------------------------------
# # # Definition:
# # # Removes a specific key and returns its value.

# # # Syntax:
# # # dict.pop(key)

# # # Example:
# # # student = {"name": "Sandeep", "age": 22, "city": "Kathmandu"}

# # # age = student.pop("age")
# # # print("Removed value:", age)
# # # print(student)

# # # Output:
# # # Removed value: 22
# # # {'name': 'Sandeep', 'city': 'Kathmandu'}

# # # --------------------------------
# # # 2. del dict[key]
# # # --------------------------------
# # # Definition:
# # # Deletes a specific key (does not return value).

# # # Example:
# # # del student["city"]
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 22}

# # # --------------------------------
# # # 3. popitem()
# # # --------------------------------
# # # Definition:
# # # Removes the last inserted key-value pair.

# # # Example:
# # # removed = student.popitem()
# # # print("Removed item:", removed)

# # # Output:
# # # ('city', 'Kathmandu')

# # # Use case:
# # # • Acts like stack (LIFO)
# # # • Undo last inserted entry

# # # --------------------------------
# # # 4. clear()
# # # --------------------------------
# # # Definition:
# # # Removes all items from the dictionary.

# # # Example:
# # # student.clear()
# # # print(student)

# # # Output:
# # # {}

# # # ------------------------------------------------
# # # SUMMARY TABLE
# # # ------------------------------------------------
# # # Method        Action                         Returns
# # # pop(key)      Remove specific key            Value
# # # del[key]      Delete key                     None
# # # popitem()     Remove last inserted pair      (key, value)
# # # clear()       Remove all items               None

# # # ------------------------------------------------
# # # 5. LOOPING DICTIONARIES
# # # ------------------------------------------------
# # # Definition:
# # # Iterating through dictionary keys, values, or key-value pairs.

# # # # Example:
# # student = {
# #     "name": "Sandeep",
# #     "age": 22,
# #     "city": "Kathmandu"
# #     }


# # # # Loop keys
# # # for key in student:
# # #     print(key)

# # # # Loop values
# # # for value in student.values():
# # #     print(value)

# # # # Loop key-value pairs
# # for key, value in student.items():
# #     print(key, ":", value)

# # # ------------------------------------------------
# # # 6. COPY DICTIONARY
# # # ------------------------------------------------
# # # Definition:
# # # Creates a shallow copy of a dictionary.

# # # Why use:
# # # • Backup data
# # # • Work on copy without changing original

# # # Example:
# # # student_copy = student.copy()
# # # student_copy["age"] = 25

# # # ------------------------------------------------
# # # 7. NESTED DICTIONARY
# # # ------------------------------------------------
# # # Definition:
# # # A dictionary inside another dictionary.

# # # Example:
# # # students = {

# # #     "s1": {"name": "Sandeep", "age": 22},
# # #     "s2": {"name": "Rita", "age": 21}
# # # }

# # # Access:
# # # print(students["s1"]["name"])  # Sandeep

# # # Use case:
# # # • School database
# # # • Employee records

# # # ------------------------------------------------
# # # 8. DICTIONARY METHODS
# # # ------------------------------------------------
# # # get()       → Safe access
# # # keys()      → All keys
# # # values()    → All values
# # # items()     → Key-value pairs
# # # pop()       → Remove key
# # # popitem()   → Remove last item
# # # update()    → Add or update items
# # # clear()     → Remove all items
# # # copy()      → Shallow copy

# # # ------------------------------------------------
# # #  TIPS
# # # ------------------------------------------------
# # # • Dictionaries are unordered and mutable
# # # • Keys must be unique
# # # • Use get() for safe access
# # # • Use items() for looping
# # # • Use nested dictionaries for complex data


# # d1 = {
# #     'name': 'sandip',
# #     'age': 22

# # }

# # d2 = {
# #     'class': 'ten',
# #     'roll': 22

# # }

# # d1.update(d2)
# # print(d1)


# # marks ={
# #     'ram':50,
# #     'shaym':65,
# #     'hari':88
# # }
# # print(max(marks.values()))


# data ={
#     'a':3,
#     'b':1,
#     'c':2
# }

# sorted_data = sorted(data.items(), key =lambda x :x[1])
# print(sorted_data)

# # # ================================================
# # # PYTHON DICTIONARIES – COMPLETE NOTES
# # # ================================================

# # # DEFINITION:
# # # A dictionary is an unordered and mutable collection of key:value pairs in Python.
# # # - Keys must be unique
# # # - Values can be of any data type

# # # WHY USE DICTIONARIES:
# # # • Store data in key-value format
# # # # • Fast lookup using keys
# # # # • Useful for student records, phonebooks, user profiles, configurations


# # # student = {
# # # "name":"ram",
# # # "age": 21,
# # # "address": "ktm"
# # # }
# # # print(student)

# student = {"name": "ram", "age": 21, "address": "ktm"}
# print(student)

# # # SYNTAX:
# # # my_dict = {"key1": value1, "key2": value2}

# # # ------------------------------------------------
# # # 1. ACCESS ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Retrieve value from a dictionary using a key.

# # # Why use:
# # # To access specific data.

# # # Example:

# # # student = {
# # #     "name": "ram",
# # #     "age": 22,
# # #     "age": 22,
# # #     "city": "Kathmandu",
# # # }


# # # print(student["city"])
# # # print(student.get("grade"))  # None


# # # Sandeep

# # # print(student.get("age"))  # 22

# # # --------------------------------
# # # Example 1: Normal get()
# # # --------------------------------
# # # print(student.get("age"))    # 22
# # # print(student.get("name"))   # Sandeep

# # # Explanation:
# # # • "age" key exists → returns value 22
# # # • "name" key exists → returns value "Sandeep"

# # # --------------------------------
# # # Example 2: Key not present
# # # # --------------------------------
# # # print(student.get("grade"))  # None

# # # Explanation:
# # # • "grade" key does not exist
# # # • No error occurs, returns None

# # # --------------------------------
# # # Example 3: Key not present with default value
# # # --------------------------------
# # # print(student.get("grade", "Not Assigned"))  # Not Assigned

# # # Explanation:
# # # • Key not found → default value is returned

# # # --------------------------------
# # # Why get() is better than dict[key]
# # # --------------------------------
# # # # Using [] → Error if key is missing
# # # # print(student["grade"])   # KeyError

# # # # Using get() → Safe
# # # print(student.get("grade")) # None (no error)

# # # Use cases:
# # # • Student database → get marks safely
# # # • Configuration files → access optional settings safely

# # # Real-world examples:
# # # • Get student's age
# # # • Get product price

# # # ------------------------------------------------
# # # 2. CHANGE ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Update the value of an existing key.

# # # Example:
# # # student={'name': 'Sandeep', 'age': 22, 'city': 'Kathmandu'}
# # # student["age"] = 23
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu'}

# # # Real-world use:
# # # • Update student marks
# # # • Update product price

# # # ------------------------------------------------
# # # 3. ADD ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Add a new key-value pair to the dictionary.

# # # Example:
# # # student["grade"] = "A"
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu', 'grade': 'A'}

# # # Real-world use:
# # # • Add new student information
# # # • Add new product details

# # # ------------------------------------------------
# # # 4. REMOVE ITEMS
# # # ------------------------------------------------
# # # Definition:
# # # Removing key:value pairs from a dictionary.

# # # Why use:
# # # • Remove outdated data
# # # • Remove incorrect entries
# # # • Clean database or configuration data

# # # --------------------------------
# # # 1. pop(key)
# # # --------------------------------
# # # Definition:
# # # Removes a specific key and returns its value.

# # # Syntax:
# # # dict.pop(key)

# # # Example:
# # # student = {"name": "Sandeep", "age": 22, "city": "Kathmandu"}

# # # age = student.pop("age")
# # # print("Removed value:", age)
# # # print(student)

# # # Output:
# # # Removed value: 22
# # # {'name': 'Sandeep', 'city': 'Kathmandu'}

# # # --------------------------------
# # # 2. del dict[key]
# # # --------------------------------
# # # Definition:
# # # Deletes a specific key (does not return value).

# # # Example:
# # # del student["city"]
# # # print(student)

# # # Output:
# # # {'name': 'Sandeep', 'age': 22}

# # # --------------------------------
# # # 3. popitem()
# # # --------------------------------
# # # Definition:
# # # Removes the last inserted key-value pair.

# # # Example:
# # # removed = student.popitem()
# # # print("Removed item:", removed)

# # # Output:
# # # ('city', 'Kathmandu')

# # # Use case:
# # # • Acts like stack (LIFO)
# # # • Undo last inserted entry

# # # --------------------------------
# # # 4. clear()
# # # --------------------------------
# # # Definition:
# # # Removes all items from the dictionary.

# # # Example:
# # # student.clear()
# # # print(student)

# # # Output:
# # # {}

# # # ------------------------------------------------
# # # SUMMARY TABLE
# # # ------------------------------------------------
# # # Method        Action                         Returns
# # # pop(key)      Remove specific key            Value
# # # del[key]      Delete key                     None
# # # popitem()     Remove last inserted pair      (key, value)
# # # clear()       Remove all items               None

# # # ------------------------------------------------
# # # 5. LOOPING DICTIONARIES
# # # ------------------------------------------------
# # # Definition:
# # # Iterating through dictionary keys, values, or key-value pairs.

# # # # Example:
# # student = {
# #     "name": "Sandeep",
# #     "age": 22,
# #     "city": "Kathmandu"
# #     }


# # # # Loop keys
# # # for key in student:
# # #     print(key)

# # # # Loop values
# # # # for value in student.values():
# # # #     print(value)

# # # # # Loop key-value pairs
# # # for key, value in student.items():
# # #     print(key, ":", value)

# # # # ------------------------------------------------
# # # # 6. COPY DICTIONARY
# # # # ------------------------------------------------
# # # # Definition:
# # # # Creates a shallow copy of a dictionary.

# # # # Why use:
# # # # • Backup data
# # # # • Work on copy without changing original

# # # # Example:
# # # # student_copy = student.copy()
# # # # student_copy["age"] = 25

# # # # ------------------------------------------------
# # # # 7. NESTED DICTIONARY
# # # # ------------------------------------------------
# # # # Definition:
# # # # A dictionary inside another dictionary.

# # # # Example:
# # # # students = {

# # # #     "s1": {"name": "Sandeep", "age": 22},
# # # #     "s2": {"name": "Rita", "age": 21}
# # # # }

# # # # Access:
# # # # print(students["s1"]["name"])  # Sandeep

# # # # Use case:
# # # # • School database
# # # # • Employee records

# # # # ------------------------------------------------
# # # # 8. DICTIONARY METHODS
# # # # ------------------------------------------------
# # # # get()       → Safe access
# # # # keys()      → All keys
# # # # values()    → All values
# # # # items()     → Key-value pairs
# # # # pop()       → Remove key
# # # # popitem()   → Remove last item
# # # # update()    → Add or update items
# # # # clear()     → Remove all items
# # # # copy()      → Shallow copy

# # # # ------------------------------------------------
# # # #  TIPS
# # # # ------------------------------------------------
# # # # • Dictionaries are unordered and mutable
# # # # • Keys must be unique
# # # # • Use get() for safe access
# # # # • Use items() for looping
# # # # • Use nested dictionaries for complex data


# # # d1 = {
# # #     'name': 'sandip',
# # #     'age': 22

# # # }

# # # d2 = {
# # #     'class': 'ten',
# # #     'roll': 22

# # # }

# # # d1.update(d2)
# # # print(d1)


# # # marks ={
# # #     'ram':50,
# # #     'shaym':65,
# # #     'hari':88
# # # }
# # # print(max(marks.values()))


# # data ={
# #     'a':3,
# #     'b':1,
# #     'c':2
# # }

# # sorted_data = sorted(data.items(), key =lambda x :x[1])
# # print(sorted_data)

# # 1. Create a dictionary of 5 students with their marks.

# # students = {
# #     "s1": {"name": "ram", "marks": 12},
# #     "s2": {"name": "mohan", "marks": 20},
# #     "s3": {"name": "hari", "marks": 30},
# #     "s4": {"name": "sita", "marks": 40},
# #     "s5": {"name": "gita", "marks": 60},
# # }

# # print(students["s1"])
# # print(students["s2"])
# # print(students["s3"])
# # print(students["s4"])
# # print(students["s5"])


# # # 2. Write a program to access the value of a specific key in a dictionary.
# # mt = {
# #     'ram':50,
# #     'shyam':65,
# #     'hari':88
# # }

# # print(mt.get('shyam'))

# # 3. Add a new key-value pair to an existing dictionary.

# stut = {"name": "nishant", "age": 21, "address": "Thaiba"}

# stut["age"] = 23
# print(stut)


# # 4. Update the value of an existing key in a dictionary.

# stut1 = {"name": "nishant", "age": 21, "address": "Thaiba"}

# stut1.update({"faculty": "BCA"})
# print(stut1)


# # 5. Delete a key from a dictionary using del.

# stut1.pop("age")
# print(stut1)

# # 6. Delete the last inserted item using popitem().

# # stut1.popitem()
# # print(stut1)

# # 7. Find the length of a dictionary.
# length = len(stut1)
# print(length)


# # 8. Check whether a key exists in a dictionary or not.

# print("name" in stut1)

# # 9. Print all keys of a dictionary.
# for keys in stut1:
#     print(keys)


# # 10. Print all values of a dictionary.
# for values in stut1.values():
#     print(values)


# # 11. Print both keys and values using loop.
# for keys, values in stut1.items():
#     print(keys, values)


# # 12. Create a dictionary from two lists using zip().
# keys1 = ["name", "age", "address", "Roll_No"]
# values1 = ["Nishant", 21, "Ktm", 14]

# my_dict = dict(zip(keys1, values1))
# print(my_dict)

# # 13. Count the frequency of characters in a string using dictionary.
# txt = "nishant"
# char_freq = {}

# for char in txt:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1

# print(char_freq)

# Example with a string
#
# 14. Merge two dictionaries into one.

# dict1 = {"name": "Nishant", "age": 22, "city": "Kathmandu"}

# dict2 = {"name1": "hare", "age1": 30, "city1": "Lalitpur"}

# dict1.update(dict2)
# print(dict1)

# # 15. Sort a dictionary by keys.
# # 16. Sort a dictionary by values.


# dxt1 = {
#     "a": 2,
#     "c": 5,
#     "b": 90,
# }
# srted_dct = dict(sorted(dxt1.items()))
# print(srted_dct)

# # 17. Find the highest value in a dictionary.

# prices = {
#     "a": 250,
#     "c": 5000,
#     "b": 90,
# }

# print(max(prices))
# 18. Find the lowest value in a dictionary.

# print(min(prices))

# 19. Create a nested dictionary for student details.


# studentDetails = {
#     "student1": {
#         "Name": "Nishant",
#         "Address": "Thiaba",
#         "Roll no": 14,
#         "Faculty": "BCA",
#     },
#     "student2": {
#         "Name": "Ishwor",
#         "Address": "Chapagaun",
#         "Roll no": 32,
#         "Faculty": "BCA",
#     },
# }

# print(studentDetails)


# 20. Write a program to store employee name and salary in dictionary.

# employee = {"Name": "John wick", "Salary": 200000}

# for values in employee.values():
#     print(values)


# # 21. Convert dictionary keys into a list.

# list_c = list(dict(employee))
# print(list_c)

# # 22. Convert dictionary values into a tuple.

# tuple_c = tuple(dict.values(employee))
# print(tuple_c)

# 23. Clear all items from a dictionary.

# print(employee.clear())


# 24. Copy one dictionary into another.
dict1 = {
    "Name": "Ishwor",
    "Address": "Chapagaun",
    "Roll no": 32,
    "Faculty": "BCA",
}
dict2 = {
    "Name": "sujan",
    "Address": "Lalitpur",
    "Roll no": 33,
    "Faculty": "BBM",
}

print(dict2.copy())
# x = dict1.copy()
# print(x)


# 25. Create a dictionary using dictionary comprehension.


# 26. Create a dictionary of numbers from 1 to 10 with their squares.
# num = {
#     "1": 1,
#     "2": 4,
#     "3": 9,
#     "4": 16,
#     "5": 25,
#     "6": 36,
#     "7": 49,
#     "8": 64,
#     "9": 81,
#     "10": 100,
# }

# print(num)

# 27. Remove duplicate values from a dictionary.
student = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}

nums = {}

for key, value in student.items():
    if value not in nums.values():
        nums[key] = value

print(nums)


# 28. Count how many times each word appears in a sentence.


print(list(dict2.keys()).count("Name"))


# 29. Find common keys between two dictionaries.

print(dict1.keys() & dict2.keys())


for key in dict1:
    if key in dict2:
        print(key)

# 30. Swap keys and values of a dictionary.

my_dict = {"a": 2, "b": 4, "c": 9}
swapped_dict = {value: key for key, value in my_dict.items()}
print(swapped_dict)
