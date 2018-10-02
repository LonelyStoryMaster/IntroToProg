menu_options = ["c - Number of non-whitespace characters",
                "w - Number of words",
                "f - Fix capitilization",
                "r - Replace punctuation",
                "s - Shorten spaces",
                "q - Quit"]
whitespaces = [' ', '\t', '\n']
punctuation = ['!', '.', ',', '?']
user_option = ' '

def menu():
    global user_option
    print("\nMENU")
    for option in menu_options:
        print(option)
    user_option = input("\nChoose an option: ")

def count_nonws(user_text):
    count = 1
    for ch in  user_text:
        if ch not in whitespaces:
            count += 1
    print("Number of non-whitespace characters:", count)

def count_words(user_text):
    text = user_text.split()
    count = len(text)
    print("Number of words:", count)

def capitalize_words(user_text):
    cap_count = 0
    return_text = ''
    edited = user_text.split()
    #Capitalizing words that come after a period
    edited[0] = edited[0].capitalize()
    for i in range(len(edited)):
        if edited[i][-1] == '.':
            cap_count += 1
            if i == len(edited) - 1:
                edited[0] = edited[0].capitalize()
            else:
                edited[i + 1] = edited[i + 1].capitalize()
    for x in range(len(edited)):
        if x == len(edited):
            return_text += edited[x]
        else:
            return_text += edited[x] + spacing[x]
    print("Spacing:", spacing)
    print("Words:", edited)
    print("Edited text:", return_text)
    #print("Number of letters capitalized:", cap_count)
    
def shorten_spaces(user_text):
    return_text = ''
    edited = user_text.split()
    for word in edited:
        if word == edited[-1]:
            return_text += word
        else:
            return_text += word + ' '

menu_functions = {'c': count_nonws, 'w': count_words, 'f': capitalize_words,
                  's': shorten_spaces}

if __name__ == '__main__':
    user_text = input("Enter a sample text:\n")
    print("\nYou entered:", user_text)
    while user_option != 'q':
        menu()
        if user_option in menu_functions:
            menu_functions[user_option](user_text)
