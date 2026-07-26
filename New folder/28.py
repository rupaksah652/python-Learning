n=int(input('enter the value of n:'))
result=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    result=result+i/fact
    print('the',i,'th number is', result)
     #print('the',i,'th number is', result)