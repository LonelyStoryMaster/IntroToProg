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
    number_parts = number.split('-')
    for part in number_parts:
        part_index = number_parts.index(part)
        parts = []
        for ch in part:
            try:
                ch = int(ch)
            except ValueError:
                for i in range(2, 10):
                    if ch in letter_numbers[i]:
                        parts.append(i)
                        continue
                    else:
                        print("Error: Unexpected character")
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
    print(count)
    return count

def count_vowels(string):
    vowels = ['e', 'y', 'u', 'i', 'o', 'a']
    count = 0
    for ch in string.lower():
        if ch in vowels:
            count += 1
    print(count)
    return count

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