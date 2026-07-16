#working with the mathematical formula
#mean squared error
import numpy as np
actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)

def mse(actual,predicted):
    return np.mean((actual - predicted)**2)

a=mse(actual,predicted)
print(a)