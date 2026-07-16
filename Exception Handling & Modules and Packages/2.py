#catching speci fic exception

try:
    m=5
    f=open('sample.txt','r')
    print(f.read())
    print(m)
    print(5/2)
    l=[1,2,3]
    l[100]
except FileNotFoundError:
    print('file not found')

except NameError:
    print('variable not defined')

except ZeroDivisionError:
    print("can't divide by zero")

except Exception as e:
    print(e)   