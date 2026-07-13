
import math
# Looping statement
# i = 1
# while i < 6:
#     print(i)

#     i += 1

# Create a variable i with the value 0
# Write a while loop that runs as long as i is less than 6
# Inside the loop: increment i by 1
# If i equals 3, use continue to skip that iteration
# Print i

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# for loops
fruits = ["apple", "banana", "Orange"]
for fruit in fruits:
    print(fruit)

# Example 1: Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i

    print("Sum", total)

# Example 2: Multiplication Table
num = 20

for i in range(1, 11):
    print(num, "x", i, "=", num)


# count even numbers
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += i
        print("Even numbers =", count)


# print a factorial numbers using for loop

num = 5




