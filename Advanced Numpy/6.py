#working with the mathematical formula
import numpy as np
#sigmoid function
def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

a=np.arange(5)
b=sigmoid(a)
print(b)

