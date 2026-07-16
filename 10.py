email=input('enter the email:')
password=input('enter the password:')

if email=='nitish.campusx@gmail.com' and password=='1234':
    print('you are welcome')

elif email!='nitish.campusx@gmail.com' and password=='1234':
    print('incorrect email')
    email=input('enter email again:')
    if email=='nitish.campusx@gmail.com':
        print('you are welcome')
    else:
        print('beta tumse na ho payega')


elif email=='nitish.campusx@gmail.com' and password!='1234':
    print('incorrect password')
    password=input('enter the password again:')

    if password=='1234':
      print('finally welcome')
    else:
      print('beta tumse na ho payega')

else:
       print('this is not correct email and password')