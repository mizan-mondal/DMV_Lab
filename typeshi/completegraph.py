import networkx as nx
import matplotlib.pyplot as plt
n = 0
while n <= 3:
    n = int(input("Enter number of vertices (must be > 3): "))
G = nx.complete_graph(n)
fig, ax = plt.subplots()
ax.set_title(f"Complete Graph with {n} Vertices")
nx.draw(G, with_labels=True, node_color='lightgreen', edge_color='gray')
plt.show()