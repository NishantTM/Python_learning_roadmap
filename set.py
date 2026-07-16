# Python Sets  
# # Definition:
# # A set is an unordered collection of unique items.
# # Duplicate values are not allowed.





# # Why use / Reason:
# # Store unique items
# # Perform operations like union, intersection
# # Fast membership test
# # Useful for unique IDs, unique elements in a list, removing duplicates

# # Syntax:
# my_set = {1, 2, 3,3} 
# print(my_set)

# # Access Set Item-------------
# # Definition: Sets are unordered, so indexing is not possible
# # Why use: Check if item exists using in




# fruits = {"apple", "banana", "mango"}
# print("apple" in fruits)   # True
# print("grape" in fruits)   # False


# # Real-world: Check if student ID exists in registered list



# # Add Set Item-------------

# # Definition: Add single item using add()
# # Why use: Insert new unique element 

# fruits = {"apple", "banana"}
# fruits.add("mango")
# print(fruits)

# {'apple', 'banana', 'mango'}
# # Real-world: Add new unique product ID

# # Remove Set Item---------------
# # Definition: Remove item using:
# # remove(value) → throws error if not exist
# # discard(value) → no error if not exist
# # Why use: Delete specific item

fruits = {"apple", "banana", "mango"}
fruits.discard("banana")
print(fruits)

# fruits.discard("grape")  # No error
# print(fruits)


# # Real-world: Remove a discontinued product
# # Loop Sets
# # Definition: Iterate through set items
# # Why use: Process each item


# # loop
# fruits = {"apple", "banana", "mango"}
# for fruit in fruits:
#     print(fruit)

# # Real-world: Print all registered students, all product IDs



# #  Join Sets
# # Definition: Combine two sets
# # Methods:
# # union() → all unique elements
# # update() → add items from another set

# a = {1,2,3}
# b = {3,4,5}
# c = a.union(b)

# print(c)  
# # # {1,2,3,4,5}

# a.update(b)
# print(a) 
# # {1,2,3,4,5}
# # Real-world: Merge two class student lists, merge two datasets

# # Frozenset
# # Definition: Immutable set, cannot add/remove items
# # Why use: Store fixed unique elements

# fs = frozenset([1,2,3])
# print(fs)
# fs.add(4)  #  Error


# # Real-world: Store unchangeable configuration values, constant IDs


# # Method of List




# # 1add()
# # Definition: Add single item to set
# # Why use: To insert a new unique element

# s = {1, 2, 3}
# s.add(4)
# print(s)
# # Output (order may vary):
# # {1, 2, 3, 4}
# # Use case: Add new student ID, new product ID

# #  remove()
# # Definition: Remove specific item from set
# # Why use: Delete item; gives error if item not present

# s = {1, 2, 3}
# s.remove(2)
# print(s)  
# # {1, 3}

# # Use case: Remove sold product, remove old data

# #  discard()
# # Definition: Remove specific item; no error if item not present
# # Why use: Safer than remove

# s = {1, 2, 3}
# s.discard(3)
# s.discard(5)  # no error
# print(s)

# # {1, 2}
# # Use case: Remove element if exists, ignore otherwise

# # pop()
# # Definition: Remove random item from set and return it
# # Why use: Remove element when order doesn’t matter

# s = {1, 2, 3}
# item = s.pop()
# print("Removed:", item)
# print("Set now:", s)

# # Removed: 1
# # Set now: {2, 3}
# # Use case: Remove arbitrary task, random selection

# # clear()
# # Definition: Remove all items from set
# # Why use: Empty the set
# s = {1, 2, 3}
# s.clear()
# print(s)

# # set()
# # Use case: Reset student list, clear dataset

# # union()
# # Definition: Combine two sets; all unique items
# # Why use: Merge sets without duplicates

# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.union(b)
# print(c)

# # {1, 2, 3, 4, 5}
# # Use case: Merge two class lists, combine datasets

# # update()
# # Definition: Add items from another set into current set
# # Why use: Modify original set with new items

# a = {1, 2, 3}
# b = {4, 5}
# a.update(b)
# print(a)

# # {1, 2, 3, 4, 5}
# # Use case: Add new students to existing set

# # intersection()
# # Definition: Return common items in two sets
# # Why use: Find items present in both sets

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))

# # {2, 3}
# # Use case: Find students in both class A and B, common products

# # difference()
# # Definition: Return items in first set but not in second
# # Why use: Find unique items in one set

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.difference(b))

# # {1}
# # Use case: Students only in class A, products only in warehouse A

# # symmetric_difference()
# # Definition: Return items in either set but not both
# # Why use: Find items that are unique to each set

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.symmetric_difference(b))

# # {1, 4}
# # Use case: Items only in A or B, but not in both


  
# s = 1
# while s <6:
#     s+=1
#     if s ==3:
#         continue
#     print(s)
    
      
      
# for i in range (1,11):
#     for s in range (1,11):
#         print({i *s})
        
    
    




# for i in range (1,11):
#     print(f'\nTable of {i}')  
#     for s in range(1,11):
#         print (f'{i} * {s} = {i*s}')




# a = {1,2,3}
# b = {4,5}
# print(a.isdisjoint(b))


# fz = frozenset(["ram"])

# name = {"ram","sita","gita"}
num = {1,2,3,4,5,4,5,3,6}
print(num)
