#Else
try:
    f=open('sample.txt','r')
except FileNotFoundError:
    print('file not found')
except Exception:
    print('somthing is wrong')
else:
    print(f.read())             