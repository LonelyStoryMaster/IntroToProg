def intials():
    user_name = input("Enter your name separated by spaces:\n")
    name_parts = user_name.split()
    initials = ''
    for part in name_parts:
        initials += part[0] + '. '
    print(initials)

def letters_to_telephone():
    letter_numbers = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'],
                      6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'],
                      9: ['W', 'X', 'Y', 'Z']}
    number = input("Enter a telephone number in the format XXX-XXX-XXXX:\n")
    number = number.upper()
    number_parts = number.split('-')
    for part in number_parts:
        part_index = number_parts.index(part)
        parts = []
        for ch in part:
            try:
                ch = int(ch)
            except ValueError:
                for letter in letter_numbers:
                    if ch in letter_numbers[letter]:
                        parts.append(letter)
                        continue
                    # else:
                    #     print("Error: Unexpected character: %s" % ch)
            else:
                parts.append(ch)
        new_part = ''
        for ch in parts:
            new_part += str(ch)
        number_parts[part_index] = new_part
    print("%s-%s-%s" % (number_parts[0], number_parts[1], number_parts[2]))

def count_consonants(string):
    consonants = ['q', 'w', 'r', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    count = 0
    for ch in string.lower():
        if ch in consonants:
            count += 1
    print("Number of consonants found:", count)
    return count

def count_vowels(string):
    vowels = ['e', 'y', 'u', 'i', 'o', 'a']
    count = 0
    for ch in string.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels found:", count)
    return count

def count_things():
    user_input = input("Please enter a string:\n")
    user_input = user_input.lower()
    count_consonants(user_input)
    count_vowels(user_input)

def pig_latin():
    sentance = input("Enter a phrase to be translated:\n")
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
    print(pig_sentance)
    return pig_sentance

if __name__ == '__main__':
    # intials()
    letters_to_telephone()
    # count_things()