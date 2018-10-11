user_string = ''
words = []
comma = ","
comma_found = False
done = False

def get_string():
    global user_string, comma_found, done
    while comma not in user_string:
        print("Error: No comma found.\n")
        user_string = input("Enter input string:\n")
    else:
        comma_found = True
    if comma_found:
        split_string()
        print("First word: %s" % words[0])
        print("Second word: %s\n" % words[1])

def split_string():
    global words
    words = user_string.split(comma)
    for word in words:
        words[words.index(word)] = word.strip()

if __name__ == "__main__":
    while user_string != 'q':
        user_string = input("Enter input string:\n")
        get_string()