import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes=[20,45,15,5,5]

plt.pie(sizes, labels=labels)

plt.grid(True)
plt.show()
