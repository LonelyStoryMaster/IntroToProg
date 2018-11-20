import os

def get_file(user_path):
    while os.path.exists(user_path) != True:
        print("Path doesn't exist. Try again.")
        user_path = input("Enter the path to a sample text:\n")
    else:
        user_file = open(user_path, 'r')
        user_text = user_file.read()
        print("The file contains:\n%s" % user_text)
        user_file.close()
    return user_text

def write_file(user_path, user_text):
    while os.path.exists(user_path) != True:
        print("Path doesn't exist. Try again.")
        user_path = input("Enter the path to a sample text:\n")
    else:
        user_file = open(user_path, 'a')
        user_file.write('\n'+user_text)
        user_file.close()

def pig_latin(user_path):
    sentance = get_file(user_path)
    pig_sentance = ''
    sentance = sentance.upper()
    words = sentance.split()
    for word in words:
        letters = []
        for ch in word:
            letters.append(ch)
        letter = letters.pop(0)
        letters.append(letter)
        letters.append('AY')
        new_word = ''
        for ch in letters:
            new_word += ch
        pig_sentance += new_word + ' '
    print("Here is the file contents in pig latin:\n%s" % pig_sentance)
    return pig_sentance

if __name__ == '__main__':
    user_path = input("Enter the path to a sample text:\n")
    write_file(user_path, pig_latin(user_path))