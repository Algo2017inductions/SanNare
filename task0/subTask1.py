#Simulations for Jasmine's curtain problem
def SobhaMethod(stack,req):
    got = False
    stack.reverse()
    for x in stack:
        if x >= req:
            if x == req:
                stack.remove(x)
            else:
                stack[stack.index(x)]-=req
            got = True
            break
    if not got:
        print('Required size not present!')
    stack.reverse()

def KamalMethod(stack,req):
    temp = list(stack)
    m = min(stack)
    got = False
    while len(temp) != 0:
        if m >= req:
            if m == req:
                stack.reverse()
                stack.remove(m)
                stack.reverse()
            else:
                stack.reverse()
                stack[stack.index(m)] -= req
                stack.reverse()
            got = True
            break
        else:
            temp.reverse()
            temp.remove(m)
            temp.reverse()
            if len(temp) != 0:
                m = min(temp)
    if not got:
        print('Required size not present!')

def JasMethod(stack,req):
    temp = list(stack)
    m = max(stack)
    got = False
    while len(temp) != 0:
        if m >= req:
            if m == req:
                stack.reverse()
                stack.remove(m)
                stack.reverse()
            else:
                stack.reverse()
                stack[stack.index(m)] -= req
                stack.reverse()
            got = True
            break
        else:
            temp.reverse()
            temp.remove(m)
            temp.reverse()
            if len(temp) != 0:
                m = max(temp)
    if not got:
        print('Required size not present!')

def checkSize(stack,req):
    s1 = list(stack)
    s2 = list(stack)
    s3 = list(stack)
    SobhaMethod(s1,req)
    print('After Sobha\'s method:')
    print(s1)
    KamalMethod(s2,req)
    print('After Kamal\'s method:')
    print(s2)
    JasMethod(s3, req)
    print('After Jasmine\'s method:')
    print(s3)

curtains = []
print('Enter the sizes of curtains in the stack(starting from bottom to top:)')
ans = 'yes'
while ans == 'yes':
    curtains.append(int(input('Enter the size of a curtain:\n')))
    ans = input('Do you want to add more sizes?(yes/no)\n')
print('Your test pile of curtains is:')
print(curtains)
q = int(input('Enter the number of queries:\n'))
for i in range(0,q):
    req = int(input('Enter the curtain size required:\n'))
    checkSize(curtains,req)
    print()

