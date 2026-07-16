n=int(input('enter the a 3 digit number:'))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
print("a:",a,"b:",b,"c:",c)
print(a+b+c)