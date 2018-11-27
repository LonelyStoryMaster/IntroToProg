def figure_1012():
    user_input = ''
    while user_input != 'q':
        try:
            weight = int(input("\nEnter weight (in pounds): "))
            height = int(input("Enter height (in inches): "))

            bmi = (float(weight) / float(height * height)) * 703
            print('BMI:', bmi)
            print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
        except:
            print('Could not calculate health info.\n')

        user_input = input("Enter any key ('q' to quit): ")

def figure_1021():
    user_input = ''
    while user_input != 'q':
        try:
            weight = int(input("\nEnter weight (in pounds): "))
            height = int(input("Enter height (in inches): "))

            bmi = (float(weight) / float(height * height)) * 703
            print('BMI:', bmi)
            print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
        except ValueError:
            print('Could not calculate health info.\n')
        except ZeroDivisionError:
            print('Invalid height entered. Must be > 0.')

        user_input = input("Enter any key ('q' to quit): ")

def figure_1032():
    user_input = ''
    while user_input != 'q':
        try:    
            weight = int(input('\nEnter weight (in pounds): '))
            if weight < 0:
                raise ValueError('Invalid weight.')

            height = int(input('Enter height (in inches): '))
            if height <= 0:
                raise ValueError('Invalid height.')

            bmi = (float(weight) / float(height * height)) * 703
            print('BMI:', bmi)
            print('(CDC: 18.6-24.9 normal)\n')
            # Source www.cdc.gov

        except ValueError as excpt:
            print(excpt)
            print('Could not calculate health info.\n')

        user_input = input("Enter any key ('q' to quit): ")

def get_weight():
    weight = int(input('\nEnter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

def figure_1041():
    user_input = ''
    while user_input != 'q':
        try:
            weight = get_weight()
            height = get_height()

            bmi = (float(weight) / float(height * height)) * 703
            print('BMI:', bmi)
            print('(CDC: 18.6-24.9 normal)\n')
            # Source www.cdc.gov

        except ValueError as excpt:
            print(excpt)
            print('Could not calculate health info.\n')

        user_input = input('Enter any key (\'q\' to quit): ')

def figure_1051():
    nums = []
    my_file = input('\nEnter file name: ')

    try:
        print('Opening', my_file)
        rd_nums = open(my_file, 'r')  # Might cause IOError

        for line in rd_nums:
            nums.append(int(line))  # Might cause ValueError
    except IOError:
        print('Could not find', my_file)
    except ValueError:
        print('Could not read number from', my_file)
    finally:
        print('Closing', my_file)
        print('Numbers found:', ' '.join([str(n) for n in nums]))

    # Define a custom exception type
class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value

def figure_1061():
    my_num = int(input('\nEnter number: '))

    if my_num < 0:
        raise LessThanZeroError('my_num must be greater than 0')
    else:
        print('my_num:', my_num)

figure_1012()
figure_1021()
figure_1032()
figure_1041()
figure_1051()
figure_1061()