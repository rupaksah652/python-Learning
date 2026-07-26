#write a program to counrt the number of words in a string without split().

s=input('enter the string:')
l=[]
temp=' '
for i  in s:

    if i!=' ':
     temp=temp+i
    else:
       l.append(temp)
       temp=' '

l.append(temp)  
print(l)    
