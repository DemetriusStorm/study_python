"""
Search vowels in input word
"""


def search_for_vowels(word: str) -> set:
    """ Return finded vowels in word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_letters_in_phrase(phrase: str, letters: str = 'aeiou') -> set:
    """ Return letters in phrase."""
    return set(letters).intersection(set(phrase))
