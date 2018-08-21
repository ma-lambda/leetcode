import math
x, y = raw_input().split(' ')
x, y = int(x), int(y)
r = ['<','>','=']
if x == y:
    print '='
else:
    if x == 1 or y == 1:
        print r[x > y]
    if x > 4 or y > 4:
        print r[x < y]
    else:
        if x ** y == y ** x:
            print '='
        else:
            print r[x ** y > y ** x]
