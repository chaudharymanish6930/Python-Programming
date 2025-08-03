import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,7])
y = np.array([1,4,9,16,25])

plt.plot(x,y,marker='o',color='y')
plt.title("basic line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.grid(True)
plt.show()