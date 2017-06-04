def flames(n,f):
    a = list(n.lower())
    b = list(f.lower())
    for i in a:
        if i in b:
            while i in a and i in b:
                a.remove(i)
                b.remove(i)
    return len(a)+len(b)

def result(n,f):
    x = flames(n,f)
    r = x%6
    ans = 'flames'[r-1]
    if ans == 'f':
        return 'Friends'
    elif ans == 'l':
        return 'Love'
    elif ans == 'a':
        return 'Adore'
    elif ans == 'm':
        return 'Marriage'
    elif ans == 'e':
        return 'Enemy'
    else:
        return 'Sister'

n = int(input('Enter the number of test cases for matchmaking:\n'))
for i in range(0,n):
    print('Enter two names:')
    a = input()
    b = input()
    print('Result: %s'%result(a,b))
