import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(1000000000), 12)
b = random.sample(range(1000000000), 12)

common = []

print(a)
print(b)

if (len(a) < len(b)):
    length = len(a)
else:
    length = len(b)

for num in range(0, length):
    if (a[num] in b) and (a[num] not in common):
        common.append(a[num])

print(common)