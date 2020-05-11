import math
import random

from solutie_initiala import *
from modularity import *
from generare_vecin import generare_vecin, potrivit_comunitate

data, legaturi = read_data()
graf = graf(data, legaturi)


# Algoritmul de Simulated Annealing
# Input: max_iteratii- nr. max de iteratii, temp- temp initiala, alpha- rata de racire, min_temp- temp. de inghet
# Output: o solutie mai buna decat cea initiala
def simulated_annealing(max_iteratii, temp, alpha, min_temp):
    solutie = rafinare_solutie_initiala()
    print("Initial: " + str(solutie))
    print("Modularity: " + str(eval_solutie(solutie)))
    temp = temp_init
    while temp > min_temp:
        for k in range(max_iteratii):
            modularity_solution = eval_solutie(solutie)
            copie_solutie = solutie
            vecin = generare_vecin(copie_solutie)
            modularity_vecin = eval_solutie(vecin)
            delta = modularity_vecin - modularity_solution
            if delta > 0:
                solutie = vecin
            else:
                random_nr = random.random()
                if math.exp(delta / temp) > random_nr:
                    solutie = vecin
        temp = temp * alpha
    return solutie, eval_solutie(solutie)


sim_an, eval = simulated_annealing(200, 500, 0.01, 0.01)
print("Final:")
print(sim_an)
print("Modularity: ")
print(eval)
