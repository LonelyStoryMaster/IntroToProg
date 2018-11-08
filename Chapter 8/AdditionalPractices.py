#Problem 1
def get_rainfall():
    rainfall_stats = []
    for i in range(12):
        rainfall = float(input("How much rain in month %d:\n" % i))
        rainfall_stats.append(rainfall)
    return rainfall_stats

def display_rainfall(rainfall_stats):
    total_rainfall = 0
    for stat in rainfall_stats:
        total_rainfall += stat
    avg_rainfall = total_rainfall / len(rainfall_stats)
    max_rainfall = max(rainfall_stats)
    min_rainfall = min(rainfall_stats)
    print("\nTotal rainfall for the year: %0.2f" % total_rainfall)
    print("Average rainfall for each month: %0.2f" % avg_rainfall)
    print("Most rainfall in a month: %0.2f" % max_rainfall)
    print("Least rainfall in a month: %0.2f" % min_rainfall)

def rainfall():
   display_rainfall(get_rainfall())

#Problem 2
def show_off_list():
    totally_not_a_list = []
    usr_str = input("Please enter a sequence of integers separated by a comma for this demonstration:\n")
    usr_str = usr_str.strip()
    totally_not_a_list = usr_str.split(',')
    for value in totally_not_a_list:
        totally_not_a_list[totally_not_a_list.index(value)] = int(value)
    print("This is a non-formatted list:\n%s" % totally_not_a_list)
    print("\nThis is a sorted list:\n%s" % sorted(totally_not_a_list))
    print("\nThis is a reversely sorted list:\n%s" % sorted(totally_not_a_list, reverse=True))
    print("\nThis is a list printing out each value separately:")
    for totally_not_an_object in totally_not_a_list:
        print(totally_not_an_object, end=' ')
    print()
    print("\nThis is the first half of that unsorted list:\n%s" % totally_not_a_list[:len(totally_not_a_list) // 2])
    print("\nThis is the second half of that same list\n%s" % totally_not_a_list[len(totally_not_a_list) // 2:])
    print("\nBut as you can see, I didn't change the actual list itself:\n%s" % totally_not_a_list)
    popped_value = totally_not_a_list.pop(len(totally_not_a_list) // 2)
    print("\nLet's take out the middle value which is: %s\n%s" % (popped_value, totally_not_a_list))
    insert_pos = (len(totally_not_a_list)  // 3)
    totally_not_a_list.insert(insert_pos - 1, popped_value)
    print("\nAnd let's add it back in somewhere like at position %d in the list:\n%s" % (insert_pos, totally_not_a_list))
    totally_not_a_list.clear()
    print("\nAnd lastly, let's wipe the slate clean and start over:\n%s" % totally_not_a_list)

#Problem 3
def encrypt(codes):
    usr_str = input("Enter a message to encrypt:\n")
    encrypted_str = ''
    for ch in usr_str:
        if ch in codes:
            encrypted_str += codes[ch]
    print("Encrypted message:\n%s" % encrypted_str)
    return encrypted_str

def decrypt(codes):
    usr_str = input("Enter a message to decrypt:\n")
    decrypted_str = ''
    keys = []
    values = []
    for key, value in codes.items():
        keys.append(key)
        values.append(value)
    for ch in usr_str:
        if ch in values:
            decrypted_str += keys[values.index(ch)]
    print("Encrypted message:\n%s" % decrypted_str)
    return decrypted_str

#Problem 4
def show_off_dict(totally_not_a_dict):
    print("\nThis is a non-formatted dictionary:\n%s" % totally_not_a_dict)
    print("\nThis is all the keys from the dictionary:\n%s" % totally_not_a_dict.keys())
    print("\nThis is all the values from the dictionary:\n%s" % totally_not_a_dict.values())
    totally_not_a_dict['sandwich'] = 'food'
    print("\nLet's add a new element called 'sandwich' with the value 'food':\n%s" % totally_not_a_dict)
    totally_not_a_dict.pop('3')
    print("\nLet's remove the key '3' now:\n%s" % totally_not_a_dict)
    totally_not_a_dict.clear()
    print("Let's wipe the slate clean and restart the dictionary now:\n%s" % totally_not_a_dict)

#Running all dis
if __name__ == '__main__':
    rainfall()
    codes = {'A': '1', 'a': '♫', 'B': '2', 'b': '@', 'C': '3', 'c': '#', 'D': '4', 'd': '$', 'E': '5', 'e': '%',
             'F': '6', 'f': '^', 'G': '7', 'g': '&', 'H': '8', 'h': '*', 'I': '9', 'i': '▓', 'J': '9', 'j': ')',
             'K': '[', 'k': '{', 'L': ']', 'l': '}', 'M': '≥', 'm': '|', 'N': ';', 'n': ':', 'O': "'", 'o': '♪',
             'P': ',', 'p': '<', 'Q': '.', 'q': '>', 'R': '/', 'r': '?', 'S': '`', 's': '~', 'T': '☺', 't': '▬',
             'U': '♦', 'u': '♣', 'V': '♠', 'v': '♂', 'W': '╝', 'w': '☼', 'X': '!', 'x': '(', 'Y': '±', 'y': '►', 
             'Z': '√', 'z': '⌂', ' ': 'î', '0': 'ê', '1': 'Æ', '2': '╣', '3': '¥', '4': 'µ', '5': '╠', '6': '¿',
             '7': 'ç', '8': '└', '9': '◘', '!': '§', '*': 'δ', '+': '╧', '-': 'Σ', '/': 'ⁿ', ',': 'Ü', '.': '╕',
             '?': '╫', ':': '▀', ';': '█', '"': '├', "'": '╚', '(': '¡', ')': '╔', '_': 'Ω', '[': '╜', ']': '"',
             '{': '₧', '}': '╓'}
    encrypt(codes)
    list_to_show = [1, 423, 234235, 123, 23, 632, 123, 0.2, 32]
    show_off_list()
    dict_to_show = {'apple': 'fruit', 'red': 'color', '3': 'number'}
    show_off_dict(dict_to_show)
