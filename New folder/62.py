#write a python program to convert a stringto title case without using the title()


s=input('enter the string:')
L=[]
for i in s.split():
    L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))    