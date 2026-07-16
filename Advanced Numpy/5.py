#broadcasting
import numpy as np
#same shape
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)
print(a+b)

#different shape
c=np.arange(6).reshape(2,3)
d=np.arange(3).reshape(1,3)
print(c+d)

e=np.arange(12).reshape(4,3)
f=np.arange(3)
print(e+f)