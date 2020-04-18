def search4vowels():
    """Print and position vowels in set from input text.
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
