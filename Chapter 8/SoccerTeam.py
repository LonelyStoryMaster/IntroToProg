def sort_dict(dict_to_sort, reverse=False):
    new_dict = {}
    tup_list = sorted(dict_to_sort.items())
    # So we can sort high-to-low and not low-to-high if we want to 
    if reverse:
        tup_list.reverse()
    for tup in tup_list:
	    new_dict[tup[0]] = tup[1]
    return new_dict    

def get_players(players, num_players=1):
    for i in range(num_players):
        player_num = int(input("Enter player %d's jersey number:\n" % (i + 1)))
        player_rating = int(input("Enter player %d's rating:\n" % (i + 1)))
        print()
        players[player_num] = player_rating
    return sort_dict(players)

def print_roster(players):
    print("ROSTER")
    for jersey, rating in players.items():
        print("Jersey number: {jersey}, Rating: {rating}".format(jersey=jersey, rating=rating))
    return players

def remove_player(players):
    jersey_num = int(input("Enter a jersey number:\n"))
    if jersey_num in players:
        players.pop(jersey_num)
    else:
        jersey_num = int(input("Enter a jersey number:\n"))
    return players

def update_rating(players):
    jersey_num = int(input("Enter a jersey number:\n"))
    if jersey_num in players:
        new_rating = int(input("Enter a new rating for player:\n"))
        players[jersey_num] = new_rating
    else:
        jersey_num = int(input("Enter a jersey number:\n"))
    return players

def print_rating_roster(players):
    rating_check = int(input("Enter a rating:\n"))
    print("\nABOVE {rating_check}".format(rating_check=rating_check))
    for jersey, rating in players.items():
        if rating > rating_check:
            print("Jersey number: {jersey}, Rating: {rating}".format(jersey=jersey, rating=rating))
    return players

commands = {'o': print_roster, 'a': get_players, 'd': remove_player, 'u': update_rating, 'r': print_rating_roster}

def menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    usr_op = input("Choose an option:\n")
    return usr_op

if __name__ == '__main__':
    players = {}
    players = get_players(players, 5)
    players = print_roster(players)
    usr_op = menu()
    while usr_op != 'q':
        if usr_op in commands:
            players = commands[usr_op](players)
            usr_op = menu()
        else:
            usr_op = menu()
    else:
        pass