#write a program that can check whether a given string is palindrome or not
#eg abba,malayalam,racecar


s=input('enter the string:')
flag=True
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        flag=False
        print('not a palindrome')
        break

if flag:
    print('palindrome')    