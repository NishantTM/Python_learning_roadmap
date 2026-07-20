# # Create a set with 5 numbers and print it.
# set_1 = {1,2,3,4,6}
# print(set_1)
# # Add a new element to a set.
# add_1 = set_1.add(9)
# print(set_1)
# # Remove an element from a set using remove() and discard().
# # rm = set_1.remove(1)
# # print(set_1)

# ds = set_1.discard(6)
# print(set_1)
# # Check if an element exists in a set.

# print(4 in set_1)
# # Find the length of a set.
# print(len(set_1))

# # Create an empty set correctly (not {}) and add elements.
# set_2 = set()
# set_2.add(400)
# print(set_2)

# # Convert a list into a set.
# list_item = [4,6,8,9]
# set_item = set(list_item)
# print(set_item)

# # Remove all elements from a set.
# set_3 = {45, 80, 90, 500, 600}
# # set_3.clear()
# print(set_3.clear())

# # Iterate through a set using a loop.
# set_3 = {45, 80, 90, 500, 600}
# for s in set_3:
#     print(s)


# # Create a set with duplicate values and observe output.
# set_4 = {1,2,3,4,5,6,1,2,1,3,4,4}
# print(set_4)

# # Find union of two sets.

# set_1 = {1,2,34,45,100}
# set_2 = {12,22,34,45, 90}

# set_3 = set_1.union(set_2)
# print(set_3)


# # # Find intersection of two sets.    

# set_4 = set_1.intersection(set_2)
# print(set_4)

# # # Find difference between two sets.
# set_diff = set_1.difference(set_2)
# print(set_diff)

# # # Find symmetric difference of two sets.
# sym_diff = set_1.symmetric_difference(set_2)
# print(sym_diff)

# # Check if one set is subset of another.
# a = frozenset({"apple", "bananan", "mango"})
# b = frozenset({"grapes", "pear", "apple"})
a = {1,2,34,45,100}
b = {1,2,34,45,100,12,22,34,45, 90}
# print(a.issubset(b))
# print(a >= b)
# print(a > b)

c = {1,2, 90}
d = {3,4}
e = {9,6}
# # Check if two sets are disjoint.
# print(c.isdisjoint(d))
# print(c.isdisjoint(e))

# # Remove a random element using pop().
# print(a.pop())
# print(a)

# # Update a set with multiple elements.
c.update(d,e)
print(c)

# # Compare two sets for equality.
if c <= d:
    print("C is greater")

# # Find common elements between two lists using sets.

list1 = [1, 2, 4, 60, 90]
list2 = [12, 22, 44, 50, 90, 2]

list3 = set(list1).intersection(list2)
print(list3)