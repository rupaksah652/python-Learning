#advanced indexing
#fancy indexing
import numpy as np
a=np.arange(24).reshape(6,4)
print(a)
print(a[[0,2,3]])
print(a[[0,2,3,5]])
print(a[0:,[0,2,3]])