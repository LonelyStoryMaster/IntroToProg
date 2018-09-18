import math

paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wall_height = float(input('Enter wall height (feet):\n'))
wall_width = float(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', int(wall_area), 'square feet')
   
gallons_needed = wall_area / 350
print("Paint needed: %f gallons" % gallons_needed)

cans_needed = math.ceil(gallons_needed)
print("Cans needed: %d can(s)" % cans_needed)

print()
color_choice = input("Choose a color to paint the wall:\n")
color_cost = int(paint_colors[color_choice])
print("Cost of purchasing %s paint: $%d" % (color_choice, int(color_cost * cans_needed)))

