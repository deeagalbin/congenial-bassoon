import matplotlib.pyplot as plt

from parsare_fisier import data, graf, matrix
from solutie_initiala import *
import networkx as nx
import numpy as np

solutie_delfini = [[1, 35, 4, 41, 15], [2, 27, 28, 42, 55, 23, 32, 26, 8, 18, 29, 10, 37], [45, 3, 11], [9, 60],
                   [5, 12, 25, 52], [14, 56, 57, 58, 49, 7, 40, 6], [20, 31, 48, 43], [13, 34, 17], [46, 24],
                   [21, 38, 59, 53, 22, 44, 16, 51, 39, 19], [36, 30], [61, 33], [47, 50], [54, 62]]


def reprezentare_solutii_finale(solutie):
    legaturi = []
    for comunitate in solutie:
        for nod in comunitate:
            for j in range(len(comunitate)):
                if comunitate[j] != nod and matrix[nod - 1][comunitate[j] - 1] == 1:
                    if [comunitate[j], nod] not in legaturi:
                        legaturi.append([nod, comunitate[j]])
    print(legaturi)
    return legaturi


legatura = reprezentare_solutii_finale(solutie_delfini)

G = nx.Graph(legatura)

nx.draw(G, with_labels=True, font_size=15,
        node_color='blue', node_size=1000)
plt.show()
