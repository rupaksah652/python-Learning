#simple example of decorator 
#short-cut method

def my_decorator(func):
    def wrapper():
        print('*')
        func()
        print('**')
    return wrapper

@my_decorator
def hello():
    print('hello')

print(hello())



