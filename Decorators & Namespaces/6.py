#enclosing scope 
def outer():
    a=4
    def inner():
         
         print(a)
    inner()
    print('outer function')
a=1    
outer()
print('main program')         