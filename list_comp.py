import random

a = random.sample(range(10000000), 10) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a2 = [num for num in a if num % 2 == 0]

print(a)
print(a2)