# break and continue

print("break example:")
for number in range(1, 10):
    if number == 5:
        break
    print(number)

print("continue example:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
