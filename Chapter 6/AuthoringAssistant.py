menu_options = ["c - Number of non-whitespace characters",
                "w - Number of words",
                "f - Fix capitilization",
                "r - Replace punctuation",
                "s - Shorten spaces",
                "q - Quit"]
whitespaces = [' ', '\t', '\n']
punctuation = ['!', '.', ',', '?']
user_option = ' '
words = []

def menu():
    global user_option
    print("\nMENU")
    for option in menu_options:
        print(option)
    user_option = input("\nChoose an option: ")

def count_nonws(user_text):
    count = 0
    for ch in  user_text:
        if ch not in whitespaces:
            count += 1
    print("Number of non-whitespace characters:", count)

def count_words(user_text):
    global words
    count = 1
    word = ''
    for ch in user_text:
        if ch in whitespaces:
            words.append(word)
            word = ''
            count += 1
        else:
            word += ch
    print("Number of words:", count)

menu_functions = {'c': count_nonws, 'w': count_words}

if __name__ == '__main__':
    user_text = input("Enter a sample text:\n")
    print("\nYou entered:", user_text)
    while user_option != 'q':
        menu()
        if user_option in menu_functions:
            menu_functions[user_option](user_text)
