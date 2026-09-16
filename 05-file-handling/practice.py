# Day 5 practice

# 1. Write and read a simple text file.
with open("practice.txt", "w") as file:
    file.write("Python practice")

with open("practice.txt", "r") as file:
    print(file.read())

# 2. Handle invalid numeric input.
try:
    value = int("25")
    print("Number:", value)
except ValueError:
    print("Invalid number")

# 3. Append another line to a file.
with open("practice.txt", "a") as file:
    file.write("\nDay 5 completed")

with open("practice.txt", "r") as file:
    print(file.read())
