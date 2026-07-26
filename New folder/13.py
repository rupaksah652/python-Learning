a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))

cal=input('enter the operation:')

if cal=='+':
    print(a+b)
elif cal=='-':
    print(a-b)
elif cal=='*':
    print(a*b)
else:
    print(a/b)