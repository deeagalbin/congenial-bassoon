import matplotlib.pyplot as plt

from parsare_fisier import data, legatura, graf, matrix
from solutie_initiala import *
import networkx as nx
import numpy as np

G = nx.Graph()
for legaturi in legatura:
    G.add_edge(legaturi[0], legaturi[1])
nx.draw(G, with_labels=True)
plt.show()
