triangle_char = input('Enter a character:\n')

triangle_height = 0

try:
    triangle_height = int(input('Enter triangle height:\n'))
except ValueError:
    print("Invalid height....Defaulting to 0")
    
print('')

for row in range(triangle_height):
    print("%s" % ((triangle_char + ' ') * (row + 1)))
