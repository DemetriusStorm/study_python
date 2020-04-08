"""
"""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

letters = ['o', 'n', ' ', 't', 'a', 'p']
new_list = []
for l in letters:
    if l in plist:
        if l not in new_list:
            new_list.append(l)

plist = new_list
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
