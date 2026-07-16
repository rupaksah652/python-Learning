#advanced indexing
#boolean indexing
import numpy as np
a=np.random.randint(1,100,24).reshape(6,4)
print(a)
#find the number greater than 50
print(a[a>50])
#find out the even number
print(a[a%2==0])
#find all number greater than 50 and are even
print(a[(a>50)&(a%2==0)])
#find all numbers not divisible by 7
print(a[a%7!=0])