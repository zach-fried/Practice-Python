# Gets a word from the user and determines whether the given string is a palindrome (ie: racecar)

word = input('Please enter a word: ')

i = len(word)

for letter in word:
    if letter == word[i - 1]:
        is_palindrome = True
        i -= 1
    else:
        is_palindrome = False
        break

if is_palindrome == True:
    print('The word you entered is a palindrome!')
elif is_palindrome == False:
    print('The word you entered is not a palindrome =(')
else:
    print('ERROR')