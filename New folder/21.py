import random
jackpot=random.randint(1,100)
guess=int(input('guess the number:'))
counter=1
while guess!=jackpot:
    if guess<jackpot:
        print('wrong!,guess the higher number')
    else:
        print('wrong!,guess the lower number')

    guess=int(input('guess the number again:'))
    counter+=1

else:
 print('congratulation,u guess the correct number')
 print('you have attempt in',counter,'chances')




    