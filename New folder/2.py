#memory
#python list
a=[i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

#numpy list
import numpy as np
import sys
a=np.arange(10000000,dtype=np.int8)
print(sys.getsizeof(a))