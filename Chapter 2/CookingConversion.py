lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))
num_servings = float(input("How many servings does this make?\n"))

one_lemon_cups = lemon_juice_cups / num_servings
one_water_cups = water_cups / num_servings
one_agave_cups = agave_nectar_cups / num_servings

num_servings_recipe = [lemon_juice_cups, water_cups, agave_nectar_cups]
one_serving_recipe = [one_lemon_cups, one_water_cups, one_agave_cups]

print()
print("Lemonade ingredients - yields", num_servings, "servings")
print(num_servings_recipe[0], "cup(s) lemon juice")
print(num_servings_recipe[1], "cup(s) water")
print(num_servings_recipe[2], "cup(s) agave nectar")

print()
num_servings_make = float(input("How many servings would you like to make?\n"))

new_lemon_cups = one_serving_recipe[0] * num_servings_make
new_water_cups = one_serving_recipe[1] * num_servings_make
new_agave_cups = one_serving_recipe[2] * num_servings_make

print()
print("Lemonade ingredients - yields", num_servings_make, "servings")
print(new_lemon_cups, "cup(s) lemon juice")
print(new_water_cups, "cup(s) water")
print(new_agave_cups, "cup(s) agave nectar")

print()
print("Lemonade ingredients - yields", num_servings_make, "servings")
print(new_lemon_cups / 16, "gallon(s) lemon juice")
print(new_water_cups / 16, "gallon(s) water")
print(new_agave_cups / 16, "gallon(s) agave nectar")
