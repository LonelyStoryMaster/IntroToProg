arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print('')
# Draw arrow base (height = 3, width = 2)
for row in range(arrow_base_height):
    print("%s" % ('*' * arrow_base_width))

# Draw arrow head (width = 4)
while arrow_head_width >= 1:
    print("%s" % ('*' * arrow_head_width))
    arrow_head_width -= 1
