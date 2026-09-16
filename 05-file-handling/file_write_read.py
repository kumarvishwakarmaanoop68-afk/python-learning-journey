# Writing and reading a text file

filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Python File Handling\n")
    file.write("Learning Python step by step.")

with open(filename, "r") as file:
    content = file.read()

print(content)
