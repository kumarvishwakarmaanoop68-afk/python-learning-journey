# Day 4 function practice

# 1. Create a function that checks whether a number is even.
def is_even(number):
    return number % 2 == 0


print("Is 10 even?", is_even(10))

# 2. Create a function that returns the largest of two numbers.
def largest(a, b):
    return max(a, b)


print("Largest:", largest(25, 18))

# 3. Create a function that counts characters in a string.
def count_characters(text):
    return len(text)


print("Characters:", count_characters("Python"))
