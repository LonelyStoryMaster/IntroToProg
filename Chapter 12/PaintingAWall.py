import math
import os
import csv

def build_color_dict(color_list):
   colors = {}
   while os.path.exists(color_list) != True:
        print("Path doesn't exist. Try again.")
        color_list = input("Enter the path to a sample text:\n")
   else:
         with open(color_list) as csvfile:
            paint_reader = csv.reader(csvfile, delimiter=',')
            firstLine = True
            for line in paint_reader:
               if firstLine:
                  firstLine = False
                  continue
               colors[line[0]] = line[1]
   return colors

color_path = "F:\\CIS1415\\IntroToProgramming\\Chapter 12\\paintPrices.csv"

paint_colors = build_color_dict(color_path)

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

