# Comparison and logical operators

a = 15
b = 10

print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)

age = 20
has_id = True

if age >= 18 and has_id:
    print("Condition passed")

if age < 18 or has_id:
    print("At least one condition is true")

print("not has_id:", not has_id)
