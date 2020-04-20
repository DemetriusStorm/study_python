# def search4vowels():
#     vowels = set('aeiou')
#     word = input('Provide a word to search for vowels: ')
#     found = vowels.intersection(set(word))
#     return ''.join(list(found))


# def search_for_vowels(word: str) -> str:
#     """Print vowels, finded in input word."""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return ''.join(list(found))


# def search_for_vowels2(word: str) -> bool:
#     """ Return bool if any vowels found in a supplied word.
#         Function name in PEP8"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return bool(found)


# def search_letters_in_phrase(phrase: str, letters: str) -> set:
#     """ Return letters in phrase"""
#     return set(letters).intersection(set(phrase))


def search4vowels():
    """
    Print and position vowels in set from input text.
    Practice for fun, fun for practice.. :)
    """
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))
    if not found:
        print('In your abracadabra not volwes from set - {}'.format(vowels))
    str_word = ''.join(set(word))
    for vowel in found:
        print(str_word)
        for index, letter in enumerate(str_word):
            if vowel == letter:
                print(' ' * len(str_word[:index]) + '^')


search4vowels()
print('\nAbout this file.\n', search4vowels.__doc__)
