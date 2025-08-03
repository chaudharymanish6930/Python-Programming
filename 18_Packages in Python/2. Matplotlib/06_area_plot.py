import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,30,25,38,50]

plt.fill_between(x,y,color="y",alpha=0.4)

plt.title("Basic area Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.show()