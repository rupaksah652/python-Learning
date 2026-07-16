a=int(input('first number:'))
b=int(input('second number:'))
c=int(input('third number:'))
if  a<b and a<c:
    print('smallest is',a)
elif b<c:
    print('smallest is',b)
else:
    print('smallest is',c)
