#enclosing scope 
def outer():
    a=1
    def inner():
         nonlocal a
         a+=1
         print('inner:',a)
    inner()
    print('outer:',a)
    
outer()
print('main program')         