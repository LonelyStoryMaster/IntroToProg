import random

languages = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian',
             'Azerbaijani', 'Bangla', 'Basque', 'Belarusian', 'Bosnian',
             'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chinese (Simplified)',
             'Chinese (Traditional)', 'Corsican', 'Croatian', 'Czech',
             'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino'
             'Finnish', 'French', 'Galican', 'Georgian', 'German', 'Greek',
             'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew',
             'Hindi', 'Hmong', 'Hungarian', 'Icelanic', 'Igbo', 'Indonesian',
             'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh',
             'Kmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian',
             'Lithuanian', 'Luxembourgish', 'Macedonia', 'Malagasay', 'Malay',
             'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali',
             'Norwegian', 'Nyangi', 'Pashto', 'Persian', 'Polish', 'Portuguese',
             'Punjabi', 'Romainian', 'Russian', 'Samoan', 'SCottish Gaelic',
             'Serbian', 'Sindhi', 'Sindhala', 'Slovak', 'Slovenian', 'Somali',
             'Southern Sotho', 'Spanish', 'Sundanese', 'Swahili', 'Swedish',
             'Tajik', 'Tamil', 'Teluga', 'Thai', 'Turkish', 'Ukrainian', 'Urdu',
             'Uzbek', 'Vietnamese', 'Welsh', 'Western Frisian', 'Xhosa',
             'Yiddish', 'Yoruba', 'Zulu']

amount_langs = len(languages)

def pickLang():
    pick = random.randint(0, amount_langs - 1)
    lang = languages[pick]
    return lang

if __name__ == '__main__':
    num_cycles = int(input("How many languages?: "))
    for i in range(num_cycles):
        print("Language %d: %s" % (i + 1, pickLang()))