num = int(input('Please enter a number: '))

if num == 0:
    print('You\'ve left me with the existential question is 0 even or odd???')
elif (num % 4 == 0):
    print('You\'ve chosen a multiple of 4!!!')
elif (num % 2) == 0:
    print('EVEN!!!')
elif (num % 2) != 0:
    print('ODD!!!')
else:
    print('Error: Please enter a valid integer')