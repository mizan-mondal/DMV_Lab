import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [11, 23, 26, 29, 30]

plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")

plt.title("X-Y Axis Data Plot")

plt.grid(False)

plt.show()