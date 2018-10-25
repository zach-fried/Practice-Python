a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_5 = []

compare = int(input('Enter a number: '))

for num in a:
    if num < compare:
        less_5.append(num)

print(less_5)