#extract username from a given email
#eg if the email is nitish24singh@gmail.com 
#then the username should be nitish24singh

s=input('enter the email:')
print(s.index('@'))
pos=s.index('@')
print(s[0:pos])