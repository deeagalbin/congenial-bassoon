from random import randint

from functie_evaluare_conexitate import conex
from parsare_fisier import matrix


def potrivit_comunitate(nod, comunitate):
    potrivit = 0
    for nod_comunitate in comunitate:
        if matrix[nod - 1][nod_comunitate - 1] == 1:
            potrivit = 1
    return potrivit


def generare_vecin(comunitati):
    lungime_comunitati = len(comunitati)
    nr_comunitate = randint(0, lungime_comunitati - 1)
    index_nod = randint(0, len(comunitati[nr_comunitate]) - 1)
    nod = comunitati[nr_comunitate][index_nod]
    pus_in_comunitate = 0
    nr_comunitate_noua = randint(0, lungime_comunitati - 1)
    while pus_in_comunitate == 0 and nr_comunitate != nr_comunitate_noua:
        if potrivit_comunitate(nod, comunitati[nr_comunitate_noua]):
            comunitati[nr_comunitate_noua].append(nod)
            comunitati[nr_comunitate].remove(nod)
            pus_in_comunitate = 1
            if len(comunitati[nr_comunitate]) == 0:
                del comunitati[nr_comunitate]
                lungime_comunitati -= 1
            elif conex(comunitati[nr_comunitate]) == 0:
                pus_in_comunitate = 0
                comunitati[nr_comunitate_noua].remove(nod)
                comunitati[nr_comunitate].append(nod)
        nr_comunitate_noua = randint(0, lungime_comunitati - 1)
    return comunitati
