#decorator
#example

def my_decorator(func):
    def wrapper():
        print('*')
        func()
        print('**')
    return wrapper

def hello():
    print('hello')

def display():
    print('hello nitish')

a=my_decorator(hello)
print(a())

b=my_decorator(display)
print(b())

