# # # fruts = ("apple", "banana", "cherry", "grpaes", "watemillion")
# # # print(type(fruts))
# # # print(len(fruts))

# # # tupple1 = "Vehicles"
# # # print(type(tupple1))


# # # tupple2 = (767.90,)
# # # print(type(tupple2))

# # # print(fruts[0])
# # # print(fruts[2:4])
# # # print(fruts[:4])

# # # # updates tupples
# # # y = list(fruts)


# # # #  -----------------Tuple-------------------


# # # # # Sequance dataType
# # # # # -In python  list, tuple, range are sequence types

# # # # # -Sequence Type –
# # # # # A Sequence Type refers to an ordered collection of items.
# # # # # The items are stored in a specific order.
# # # # # Each item can be accessed using its index position.
# # # # # -Duplicate values allowed (list, tuple)


# # # # # Definition
# # # # # A tuple is an ordered collection of items that is immutable (cannot be changed) and allows duplicate values.
# # # # # Why use / Reason:

# # # # # Store multiple values together
# # # # # Keep data safe from accidental modification
# # # # # Faster than list for fixed data
# # # # # Useful for coordinates, days of the week, fixed info


# # # # # Syntax:
# # # # # my_tuple = (item1, item2, item3)


# # # # # Access Tuple------------
# # # # # 	Definition: Retrieve item from tuple using index
# # # # # 	Why use: To get specific data

# # # days = ("Sun", "Mon", "Tue", "Wed")
# # # print(days[0])


# # # # Sun print(days[-1]) # Wed
# # # # # Real-world: Get first day of week, last month of quarter


# # # # # Update Tuple ------------------
# # # # 	# Definition: Tuples are immutable, cannot change individual items directly
# # # # 	# Why use: If need to modify → convert tuple to list, update, then back to tuple

# # # fruits = ("apple", "banana", "mango")


# # # fruits_list = list(fruits)
# # # fruits_list[1] = "orange"
# # # fruits = tuple(fruits_list)
# # # print(fruits)

# # # # ('apple', 'orange', 'mango')
# # # # # Real-world: Store fixed info safely, e.g., coordinates → rarely change


# # # #  Unpack Tuple ------------------------
# # # # # Definition: Assign tuple items to separate variables
# # # # # Why use: Easily use each element

# # # # point = (10, 20, 30)
# # # # x, y, z = point
# # # # print(x, y, z)


# # # a = (1,2,3)
# # # x,y,z =a


# # # # a = 10

# # # # color = (222,333,443)
# # # # r,g,b = color
# # # # print(r,g,b)


# # # # # 10 20 30
# # # # # Real-world: Coordinates (x, y, z), RGB color values

# # # # #  Loop Tuple
# # # # # Definition: Iterate through tuple items
# # # # # Why use: Process each item
# # # # # (for loop):
# # # # fruits = ("apple", "banana", "mango")
# # # # for fruit in fruits:
# # # #     print(fruit)
# # # # #  (while loop):


# # # # i = 0
# # # # while i < len(fruits):
# # # #     print(fruits[i])
# # # #     i += 1


# # # # # Real-world: Print all months, process fixed data

# # # # # Join Tuple ----------------------------
# # # # # Definition: Combine two or more tuples
# # # # # Why use: Merge multiple fixed datasets

# # # # t1 = (1, 2, 3)
# # # # t2 = (4, 5, 6)
# # # # t3 = t1 + t2
# # # # print(t3)

# # # # # (1, 2, 3, 4, 5, 6)
# # # # # Real-world: Combine coordinates, combine student IDs

# # # # #  Tuple Methods-----
# # # # # Definition: Limited methods because tuple is immutable


# # # # num = (1,1,22,22,3,55,66,55,66,)
# # # # print(num.count(3))
# # # # # Methods:
# # # # # count(value) →
# # #
# # #
# # #
# # #
# # #
# # # Count occurrences
# # # # # index(value) → Find index of first occurrence

# # # # fruits = ("apple", "banana", "apple", "mango")
# # # # print(fruits.count("apple")) # 2
# # # # print(fruits.index("banana")) # 1
# # # # # Real-world: Count repeated items, find position of specific data

# # # # # Key Points
# # # # # Tuples are ordered, immutable, allow duplicates
# # # # # Use tuple when data is fixed or should not change
# # # # # Faster than list → useful for large datasets with fixed values
# # # # # Methods are limited → only count() and index()


# # # # # syntax----------
# # # # furits = ("apple", "banana", "cherry ")
# # # # print(furits)


# # # # #  Access Tuple-------------
# # # # days = ("Sun", "Mon", "Tue", "Wed")
# # # # print(days[2])
# # # # print(days[-1]) # Wed


# # # # #  Update Tuple------------
# # # # fruits = ("apple", "banana", "mango")
# # # # fruits_list = list(fruits)
# # # # fruits_list[1] = "orange"
# # # # fruits = tuple(fruits_list)
# # # # print(fruits)


# # # # # Output:
# # # # # ('apple', 'orange', 'mango')


# # # # # Unpack Tuple----------

# # # # point = (10, 20, 30)
# # # # x, y, z = point
# # # # print(x, y, z)
# # # # # Output:
# # # # # 10 20 30


# # # # # loop of tuple---------

# # # # fruits = ("apple", "banana", "mango")
# # # # for fruit in fruits:
# # # #     print(fruit)
# # # # #  (while loop):

# # # # fruits = ("apple", "banana", "mango")

# # # # # for i in range(len(fruits)):
# # # # #     print(i + 1, fruits[i])


# # # fruits = ("apple", "banana", "mango")

# # # for i in range(len(fruits)) :
# # #     # print(i, fruits[i])
# # #     print(f'{i}. {fruits[i]}')


# # # # i = 0
# # # # while i < len(fruits):
# # # #     print(fruits[i])
# # # #     i += 1

# # #     # i < 3
# # #     # 0+= 1 =1
# # #     # 1+= 1 =2
# # #     # 2+= 1 =3


# # # # # Join Tuple---------
# # # # # 	Definition: Combine two or more tuples
# # # # # 	Why use: Merge multiple fixed datasets

# # # # t1 = (1, 2, 3)
# # # # t2 = (4, 5, 6)
# # # # t3 = t1 + t2
# # # # print(t3)


# # # # # Output:
# # # # # (1, 2, 3, 4, 5, 6)


# # # # # Tuple Methods------
# # # # # Definition: Limited methods because tuple is immutable
# # # # # Methods:
# # # # # count(value) → Count occurrences
# # # # # index(value) → Find index of first occurrence

# # # # fruits = ("apple", "banana", "apple", "mango")
# # # # print(fruits.count("apple"))
# # # # print(fruits.index("banana"))
# # # # # Real-world: Count repeated items, find position of specific data


# # # # #WAP Join (join tuple) two tuples.

# # # # #WAP Create a tuple with 5 integers and print it.
# # # # #WAP Print the first element of a tuple.
# # # # #WAP Print the last element of a tuple.
# # # # #WAP Print the element at index 2 from a tuple.
# # # # #WAP Find and print the length of a tuple.
# # # # #WAP Print all elements of a tuple using a for loop.
# # # # #WAP Check if a number exists in a tuple and print the result.
# # # # #WAP Create a tuple with both numbers and strings and print it.


# # # fruits = ("apple", "banana", "mango")
# # # i = 0
# # # while i < len(fruits):
# # #     print(i)
# # #     i = i +1


# # day = ("sun", "mon", "tue")

# # c_day = list(day)
# # c_day[1] = "m"

# # day = tuple(c_day)
# # print(day)


# # numbers.
# # Print the first item of a tuple.

# f_item = ("1", "4", "6", "9", "10", "4", "6", "4")
# print(f_item[0])
# # Find the length of a tuple.

# print(len(f_item))
# # Count how many times 2 appears in a tuple.
# print(f_item.count("4"))

# # Find the index of "apple" in a tuple.
# fruits = ("apple", "banana", "mango", "orange")
# print(fruits.index("mango"))

# # Convert a tuple into a list.
# num = ("34", "56", "90", "60")
# list_c = list(num)
# print(list_c)

# # Convert a list into a tuple.
# list_num = [34, 90, 89, 3445, 3435]
# tuple_c = tuple(list_num)
# print(tuple_c)

# # Create a single-item tuple correctly.
# tupp_1 = ("45",)
# print(tupp_1[0])

# # Loop through all items of a tuple.
# tupple_2 = ("34", "23", "36", "23")
# for t in tupple_2:
#     print(t)

# # Concatenate two tuples.

# tp_1 = ("34", "23", "34", "23")
# tp_2 = ("44", "52", "90", "26")
# tp_join = tp_1 + tp_2
# print(tp_join)

# # # Repeat a tuple 3 times.

# name = ("ram",)

# for i in range(3):
#     for j in name:
#         print(j)
# print()

# # # Check whether an item exists in a tuple.
# print("ram" in name)


# # # Find maximum and minimum values in a tuple.
# tp_num = (45, 56, 80, 78, 400)
# mx = max(tp_num)
# print(mx)

# mi = min(tp_num)
# print(mi)

# # # Create a nested tuple and access inner elements.
# tp_ns = ("45(90)", "67(98)")
# print(tp_ns)

# # # Unpack tuple values into variables.
# point = (45, 90, 110, 780)
# a,b,c,d = point
# print(a,b,c,d )

# # # Create a tuple of student names and print each name.
stud_name = ('Nishant', 'Sujan', 'Ishwor', 'Prashant')
print(stud_name)
# # # Find the sum of all tuple elements.

total = 0
for i in range(1,15):
    total+=i
print(total)
    
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(sum(t))

# # # Slice a tuple to print last 3 elements.
# num_1 = (45, 90, 110, 780, 34, 56, 67, 78)
# slice1 = num_1[-3 :]
# print(slice1)

# # # Compare two tuples.
tp_1 = ('34', '74', '90')
tp_2 = ('45', '56', '456')
print(tp_1 == tp_2)
print(tp_1 < tp_2)

# # # Create a tuple with mixed data types.

tp = (1, 3, "Suj", "NKS", 787.09)
print(tp)
