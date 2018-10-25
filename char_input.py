import time

year = int(time.asctime().split()[4])

name_age = input('Please enter your name and age separated by a comma: ')
repeat = int(input('How many times would you like to repeat the message?: '))

name = name_age.split(',')[0]
age = int(name_age.split(',')[1])

hundred = (100 - age) + year

if repeat == 0:
    print('WHO DO YOU THINK YOU ARE BREAKING MY PROGRAM???')
else:
    while repeat > 0:
        print(name + ', you will be 100 years old in the year ' + str(hundred))
        repeat -= 1
