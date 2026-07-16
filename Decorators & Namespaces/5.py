#enclosing scope 
def outer():
    def inner():
         print('inner function')
    inner()
    print('outer function')
outer()
print('main program')          