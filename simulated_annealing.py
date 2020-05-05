import math
import random

from solutie_initiala import *
from functie_evaluare_conexitate import *
from evaluare import *
from generare_vecin import generare_vecin

data, legaturi = read_data()
graf = graf(data, legaturi)


def simulated_annealing(max_iteratii, temp, alpha, min_temp):
    solutie = communities_graph(graf, data)
    print("com initiale sunt: " + str(solutie))
    while temp > min_temp:
        print(temp)
        for k in range(0, max_iteratii):
            print(k)
            copie_solutie = solutie
            print(copie_solutie)
            vecin = generare_vecin(copie_solutie)
            print("dupa" + str(vecin))
            delta = eval_solutie(vecin) - eval_solutie(solutie)
            if delta < 0:
                solutie = vecin
            elif random.random() < math.exp(-delta / temp):
                solutie = vecin
            print("final")
        temp = alpha * temp
    return solutie


sim_an = simulated_annealing(4, 100, 0.01, 0.001)
print("Final:")
print(sim_an)
