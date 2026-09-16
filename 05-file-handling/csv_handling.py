# CSV file handling using Python's csv module

import csv

filename = "students.csv"

rows = [
    ["Name", "Course"],
    ["Anoop", "Diploma IT"],
    ["Student 2", "Python"],
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open(filename, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
