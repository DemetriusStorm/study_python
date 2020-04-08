"""
"""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist = plist[1:3] + plist[5:6] + plist[4:5] + plist[7:5:-1]
new_phrase = ''.join(plist)

print(plist)
print(new_phrase)
