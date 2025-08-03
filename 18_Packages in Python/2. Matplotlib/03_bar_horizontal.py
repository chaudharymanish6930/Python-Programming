import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [7, 13, 5, 17, 10]

plt.barh(categories, values, color='b')

plt.title("basic bar plot")
plt.xlabel("categories")
plt.ylabel("values")

plt.grid(True)
plt.show()