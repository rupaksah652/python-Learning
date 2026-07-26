lower=int(input('enter the lower value:'))
higher=int(input('enter the higher value:'))
for i in range(lower,higher+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         print(i)
