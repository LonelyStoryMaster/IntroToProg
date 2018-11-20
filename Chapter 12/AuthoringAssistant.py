import os

menu_options = ["c - Number of non-whitespace characters",
                "w - Number of words",
                "f - Fix capitalization",
                "r - Replace punctuation",
                "s - Shorten spaces",
                "q - Quit"]
whitespaces = [' ', '\t', '\n']
punctuation = ['!', '.', ',', '?']
user_option = ' '
spacing = []

def save_spacing(user_text):
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    space = ''
    for ch in user_text:
        if ch == ' ':
            space += ch
        else:
            if space != '':
                spacing.append(space)
                #print("Spaces found: [%s]" % space) # Debugging line
            space = ''

def menu():
    global user_option
    print("\nMENU")
    for option in menu_options:
        print(option)
    user_option = input("\nChoose an option:\n")

def get_num_of_non_WS_characters(user_text):
    count = 0
    for ch in  user_text:
        if ch not in whitespaces:
            count += 1
    print("Number of non-whitespace characters:", count)
    return count

def get_num_of_words(user_text):
    text = user_text.split()
    count = len(text)
    print("Number of words:", count)
    return count

def fix_capitalization(user_text):
    global spacing
    cap_count = 0
    return_text = ''
    edited = user_text.split()
    save_spacing(user_text)
    #Capitalizing words that come after a period
    edited[0] = edited[0].capitalize()
    for i in range(len(edited)):
        if (edited[i][-1] == '.') or (edited[i][-1] == ';'):
            if edited[i] == 'yes;':
                continue
            cap_count += 1
            if i == len(edited) - 1:
                edited[0] = edited[0].capitalize()
            else:
                edited[i + 1] = edited[i + 1].capitalize()
    #Putting the sentance back together
    for x in range(len(edited)):
        if x == len(spacing):
            return_text += edited[x]
        else:
            return_text += edited[x] + spacing[x]
    ''' #Debugging lines
    print("Spacing:", spacing)
    print("Words:", edited)
    '''
    print("Edited text:", return_text)
    print("Number of letters capitalized:", cap_count)
    return return_text, cap_count

def replace_punctuation(user_text, exclamationCount = 0, semicolonCount = 0):
    text = []
    return_text = ''
    for ch in user_text:
        if ch == '!':
            text.append('.')
            exclamationCount += 1
        elif ch == ';':
            text.append(',')
            semicolonCount += 1
        else:
            text.append(ch)
    for ch in text:
        return_text += ch
    print("Punctuation replaced")
    print("exclamationCount:", exclamationCount)
    print("semicolonCount:", semicolonCount)
    print("Edited text:", return_text)
    return exclamationCount, semicolonCount
    
def shorten_space(user_text):
    return_text = ''
    edited = user_text.split()
    for word in edited:
        if word == edited[-1]:
            return_text += word
        else:
            return_text += word + ' '
    print("Edited text:", return_text)
    return return_text

menu_functions = {'c': get_num_of_non_WS_characters, 'w': get_num_of_words, 'f': fix_capitalization,
                  's': shorten_space, 'r': replace_punctuation}

if __name__ == '__main__':
    # Getting the file
    user_path = input("Enter the path to a sample text:\n")
    while os.path.exists(user_path) != True:
        print("Path doesn't exist. Try again.")
        user_path = input("Enter the path to a sample text:\n")
    else:
        user_file = open(user_path, 'r')
        user_text = user_file.read()
        print("The file contains:\n%s" % user_text)
    # Actually working with it
    while user_option != 'q':
        menu()
        if user_option in menu_functions:
            menu_functions[user_option](user_text)
