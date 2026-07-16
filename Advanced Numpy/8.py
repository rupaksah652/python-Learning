#working with missing value
import numpy as np
a=np.array([1,2,3,4,5,np.nan,6])
b=a[~np.isnan(a)]
print(b)