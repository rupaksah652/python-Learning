#a big problem of decorator
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args)==data_type:
                func(*args)
            else:
                raise TypeError('i cannot be run')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

square(2) 
square('ram')        