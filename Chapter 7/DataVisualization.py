chart_title = ''
column1_title = ''
column2_title = ''
column1 = []
column2 = []

comma = ','

def get_chart_data():
    global column1, column2
    data_str = input("\nEnter a data point (-1 to stop input):\n")

    while data_str != '-1':
        int_found = False
        found_comma = False
        mult_commas = False
        if comma not in data_str:
            print("Error: No comma in string.")
        elif data_str.count(comma) > 1:
            print("Error: Too many commas in input.")
            mult_commas = True
        elif comma in data_str: 
            found_comma = True
            parts = data_str.split(comma)
            try:
                parts[1] = int(parts[1])
            except ValueError:
                print("Error: Comma not followed by an integer.")
            else:
                int_found = True
        if int_found and found_comma and  not mult_commas:
            column1.append(parts[0])
            column2.append(parts[1])
            print("Data string: %s" % parts[0])
            print("Data integer: %d" % parts [1])
        data_str = input("\nEnter a data point (-1 to stop input):\n")

def get_chart():
    global chart_title, column1_title, column2_title
    chart_title = input("Enter a title for the data:\n")
    print("You entered: %s" % chart_title)
    column1_title = input("\nEnter the column 1 header:\n")
    print("You entered: %s" % column1_title)
    column2_title = input("\nEnter the column 2 header:\n")
    print("You entered: %s" % column2_title)
    get_chart_data()

def print_table():
    print("%33s" % chart_title)
    print("%-20s|%23s" % (column1_title, column2_title))
    print("%s" % '-' * 44)
    for i in range(len(column1)):
        print("%-20s|%23d" % (column1[i], column2[i]))

def print_histogram():
    for i in range(len(column1)):
        print("%20s %s" % (column1[i], '*' * column2[i]))

if __name__ == '__main__':
    get_chart()
    print()
    print_table()
    print()
    print_histogram()