triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for row in range(triangle_height):
    print("%s" % ((triangle_char + ' ') * (row + 1)))
