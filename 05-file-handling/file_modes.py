# Common file modes

# r = read
# w = write (overwrites existing content)
# a = append
# x = create a new file

filename = "notes.txt"

with open(filename, "w") as file:
    file.write("First line\n")

with open(filename, "a") as file:
    file.write("Second line\n")

with open(filename, "r") as file:
    print(file.read())
