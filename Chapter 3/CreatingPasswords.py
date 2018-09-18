favoriteColor = input('Enter favorite color:\n')
petName = input('Enter pet\'s name:\n')
number = input('Enter a number:\n')

print('You entered:', favoriteColor, petName, number)

password1 = favoriteColor + '_' + petName
password2 = number + favoriteColor + number
print('\nFirst password:', password1)
print('Second password:', password2)

print("\nNumber of characters in %s: %d"  % (password1, len(password1)))
print("Number of characters in %s: %d" % ( password2, len(password2)))
