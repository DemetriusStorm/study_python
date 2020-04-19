"""
Search vowels in input word
"""


def search4vowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))
    return ''.join(list(found))


def search_for_vowels(word: str) -> str:
    """Print vowels, finded in input word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return ''.join(list(found))


def search_for_vowels2(word: str) -> bool:
    """ Return bool if any vowels found in a supplied word.
        Function name in PEP8"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search_for_vowels3(word: str) -> set:
    """ Return finded vowels in word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_letters_in_phrase(phrase: str, letters: str) -> set:
    """ Return letters in phrase"""
    return set(letters).intersection(set(phrase))


def search_letters_in_phrase2(phrase: str, letters: str = 'aeiou') -> set:
    """ Return letters in phrase."""
    return set(letters).intersection(set(phrase))


print(help(search_letters_in_phrase2))
print(search_letters_in_phrase2('dskjf$hskaTgfey235', 'sdfsfaWTG#$%'))
print(search_letters_in_phrase2('dskjf$hskaTgfey235', letters='sdfsfaWTG#$%'))
print(search_letters_in_phrase2(letters='sdfsfaWTG#$%', phrase='dskjf$hskaTgfey235'))
