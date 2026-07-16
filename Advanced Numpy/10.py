#plotting graph

#plotting a 2D plot
#y=x^2
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()