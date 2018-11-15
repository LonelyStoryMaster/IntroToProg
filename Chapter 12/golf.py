import os
import csv

def gather_data():
    player_data = []
    quit = False
    while quit != True:
        usr_name = input("\nEnter player's name or q to quit:\n")
        if usr_name == 'q':
            quit = True
            break
        else:
            data = []
            usr_score = input("Enter player's score:\n")
            data.append(usr_name)
            data.append(usr_score)
            player_data.append(data)
    return player_data

def save_data(player_data):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    csv_path = os.path.join(__location__, 'golf.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow(['Name','Score'])
        data_writer.writerows(player_data)
    return csv_path

def print_data(data_path):
    if os.path.exists(data_path):
        with open(data_path, 'r') as csvfile:
           data_reader = csv.reader(csvfile, delimiter=',')
           for row in data_reader:
               print("%-8s|%6s" % (row[0], row[1]))
    else:
        print("This path doesn't exist")

if __name__ == '__main__':
    print_data(save_data(gather_data()))