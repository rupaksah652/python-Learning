#plotting graph

#plotting a 2D plot
#y=sin(x)
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()