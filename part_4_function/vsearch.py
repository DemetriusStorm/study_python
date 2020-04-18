"""
Search vowels in input word
"""


def search4vowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))
    return ''.join(list(found))


print(search4vowels())
