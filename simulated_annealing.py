import math
import random

from solutie_initiala import *
from evaluare import *
from generare_vecin import generare_vecin

data, legaturi = read_data()
graf = graf(data, legaturi)


def simulated_annealing(max_iteratii, temp, alpha, min_temp):
    solutie = communities_graph(graf, data)
    print("com initiale sunt: " + str(solutie))
    print("Modularity: " + str(eval_solutie(solutie)))
    while temp > min_temp:
        for k in range(0, max_iteratii):
            copie_solutie = solutie
            vecin = generare_vecin(copie_solutie)
            delta = eval_solutie(vecin) - eval_solutie(solutie)
            if delta < 0:
                solutie = vecin
            elif random.random() < math.exp(-delta / temp):
                solutie = vecin
        temp = alpha * temp
    return solutie, eval_solutie(solutie)


sim_an, eval = simulated_annealing(10, 1000, 0.9999, 0.000001)
print("Final:")
print(sim_an)
print("Modularity: ")
print(eval)
