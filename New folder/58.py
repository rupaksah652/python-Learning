#count the frequency of a particular character in a priovided string
#eg 'hello how are you' is the string,the frequency of h in this string is 2

s=input('enter the string:')
term=input('what u want to search for:')
count=0
for i in s:
    if i==term:
        count+=1

print('the total frequency of',term,'is:',count)        