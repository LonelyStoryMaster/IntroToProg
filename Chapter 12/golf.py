def save_data(data_list):
    save_file = open("Chapter 12\\golf.txt", 'w')
    for data in data_list:
        save_file.write(str(data) + '\n')
    save_file.close()

def print_saved_data():
    save_file = open("Chapter 12\\golf.txt", 'r')
    save_lines = save_file.readlines()
    print("Player Name  |  Score")
    for line in save_lines:
        parts = line.split(',')
        for part in parts:
            parts[parts.index(part)] = part.strip()
        print("%-13s|  %s" % (parts[0], parts[1]))
    save_file.close()

def gather_data():
    data_list = []
    usr_quit = False
    while usr_quit != True:
        name = input("\nEnter player's name:\n")
        if (name == 'q'):
            usr_quit = True
            break
        else:
            score = input("Enter player's score:\n")
            data = name + ',' + score
            data_list.append(data)
    return data_list

save_data(gather_data())
print_saved_data()
