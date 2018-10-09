import math
import random

def times_ten():
    print("Timesing by 10:")
    user_num = int(input("Enter a number: "))
    print("%d times 10 is %d" % (user_num, user_num * 10))
    return user_num * 10

def get_first_name():
    print("Getting first name:")
    first_name = input("Please enter your first name: ")
    print("Enter name is:", first_name)
    return first_name

def calc_insurance():
    print("Calculation property insurance:")
    prop_price = float(input("How much is your property worth?: "))
    print("Minimum insurance to buy: %0.2f" % (prop_price * 0.8))
    return prop_price * 0.8

def auto_prices():
    print("Auto payments:")
    prices = {'loan payment':0.0, 'insurance':0.0, 'gas':0.0, 'oil':0.0,
              'tires':0.0, 'maintenance':0.0}
    total = 0.0
    for price in prices:
        prices[price] = float(input("How much is your %s per month? " % price))
        total += prices[price]
    print("Total monthly automobile cost: %0.2f" % total)
    print("Total yearly automobile cost: %0.2f" % (total * 12))
    return (total, total * 12)

def calc_prop_tax():
    print("Calculating property tax:")
    prop_price = float(input("What is the value of your property?: "))
    assess_price = prop_price * 0.6
    prop_tax = assess_price * 0.0072
    print("Assessed price: %0.2f" % assess_price)
    print("Property tax: %0.2f" % prop_tax)
    return (assess_price, prop_tax)

def calc_paint():
    print("Calculate paint job cost:")
    sqr_feet = float(input("How many sqaure feet of wall to paint?: "))
    gallon_cost = float(input("What is the price per gallon of paint?: "))
    gallons_needed = math.ceil(sqr_feet / 112)
    hrs_labor = gallons_needed * 8
    paint_cost = gallons_needed * gallon_cost
    labor_cost = hrs_labor * 35.00
    total_cost = paint_cost + labor_cost
    print("Gallons needed: %0.2f" % gallons_needed)
    print("Hours of labor: %0.2f" % hrs_labor)
    print("Cost of the paint: %0.2f" % paint_cost)
    print("Cost of the labor: %0.2f" % labor_cost)
    print("Total job cost: %0.2f" % total_cost)

def max(x, y):
    if x > y:
        return x
    else:
        return y

def get_max():
    print("Finding max of two numbers:")
    x = int(input("Enter a number: "))
    y = int(input("Enter another: "))
    print("This one is greater:", max(x, y))
    return max(x, y)

def gen_nums():
    odd_count = 0
    even_count = 0
    blah = 0
    print("Generating numbers...")
    for i in range(100):
        blah += i
        num = random.randint(0, 100)
        if (num % 2) == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even count: %d, Odd count: %d" % (even_count, odd_count))
    return even_count, odd_count

functions = {'times_ten': times_ten, 'get_first_name': get_first_name, 'calc_insurance': calc_insurance,
             'auto_prices': auto_prices, 'calc_prop_tax': calc_prop_tax, 'calc_paint': calc_paint,
             'get_max': get_max, 'gen_nums': gen_nums}

if __name__ == '__main__':
    for function in functions:
        functions[function]()
        print()