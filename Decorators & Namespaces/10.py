#anything meaningful ?
#decorator
 
import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken by',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def hello():
    print('hello world')
    time.sleep(2)

@timer
def square(num):
    time.sleep(3)
    print(num**2)

@timer
def power(a,b):
    print(a**b)

print(hello())
print(square(2))  
print(power(2,3))          