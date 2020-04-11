x = int(input('Size? '))
y = input('Symbol? ')

for r in range(x):
    for c in range(r + 1):
        print(y, end='')
    print()
    
#for r in range(x):
#    for c in range(r):
#        print(' ' + y, end='')
#    print(y)
