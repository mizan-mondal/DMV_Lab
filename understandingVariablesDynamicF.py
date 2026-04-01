import matplotlib.pyplot as plt

# Number of data points
n = int(input("Enter number of data points: "))

x = []
y = []

# Taking user input
for i in range(n):
    x_val = float(input(f"Enter X value {i+1}: "))
    y_val = float(input(f"Enter Y value {i+1}: "))
    
    x.append(x_val)
    y.append(y_val)

# Plot the graph
plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("X-Y Axis Data Plot")

plt.grid(True)

plt.show()