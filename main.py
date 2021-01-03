import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1, type="source")
G.add_node(2, type="inductor")
G.add_node(3, type="resistance")

G.add_edge(1, 2)
G.add_edge(2, 3)

labels = { key: f'{key}: {values}' for [key, values] in G.nodes.data() }

fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(15, 8))
nx.draw(G, ax=ax1, labels=labels, with_labels=True)

fig.savefig('./graph.png')