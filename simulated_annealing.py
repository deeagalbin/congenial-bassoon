import math
import random

from solutie_initiala import *
from evaluare import *
from generare_vecin import generare_vecin, potrivit_comunitate

data, legaturi = read_data()
graf = graf(data, legaturi)


#Algoritmul de Simulated Annealing
#Input: max_iteratii- nr. max de iteratii, temp- temp initiala, alpha- rata de racire, min_temp- temp. de inghet
#Output: o solutie mai buna decat cea initiala
def simulated_annealing(max_iteratii, temp, alpha, min_temp):
    solutie = communities_graph(graf, data)
    print("com initiale sunt: " + str(solutie))
    print("Modularity: " + str(eval_solutie(solutie)))
    average = eval_solutie(solutie)
    nr_parcurgeri = 1
    while temp > min_temp:
        for k in range(0, max_iteratii):
            copie_solutie = solutie
            vecin = generare_vecin(copie_solutie)
            average += eval_solutie(vecin)
            nr_parcurgeri += 1
            delta = eval_solutie(vecin) - eval_solutie(solutie)
            if delta < 0:
                solutie = vecin
            elif random.random() < math.exp(-delta / temp):
                solutie = vecin
        temp = alpha * temp
    solutie = imbunatire_solutie(solutie)
    average += eval_solutie(solutie)
    nr_parcurgeri += 1
    average_total = average / nr_parcurgeri
    print("solutie", solutie)
    print("Average: ", average_total)
    return solutie, eval_solutie(solutie)


#Imbunatatirea solutiei finale, a.i. sa eliminam comunitatile formate dintr-un singur nod
#Input: comunitatile
#Outpu: comunitatile "reorganizate"
def imbunatire_solutie(solutie):
    n = len(solutie)
    i = 0
    #iteram prin lista cu comunitati
    while i < n:
        #verificam daca comunitatea are un singur element
        if (len(solutie[i]) == 1):
            pus_in_comunitate = 0
            k = 0
            #cautam o comunitate potrivita pentru elementul unic
            while pus_in_comunitate == 0 and k < n:
                if potrivit_comunitate(solutie[i][0], solutie[k]) == 1:
                    solutie[k].append(solutie[i][0])
                    solutie.remove(solutie[i])
                    print("sol modif", solutie)
                    pus_in_comunitate = 1
                    n = n - 1
                k += 1
        else:
            i += 1
    return solutie


sim_an, eval = simulated_annealing(200, 500, 0.01, 0.01)
print("Final:")
print(sim_an)
print("Modularity: ")
print(eval)
