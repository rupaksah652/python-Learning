#plotting graph

#plotting a 2D plot
#y=xlog(x)
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x*np.log(x)
plt.plot(x,y)
plt.show()