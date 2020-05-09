from random import randint

from functie_evaluare_conexitate import conex
from parsare_fisier import matrix


def potrivit_comunitate(nod, comunitate):
    #nod-nodul pentru care verificam potrivirea
    #comunitate-comunitatea in care incercam sa il introducem
    #parcurgem comunitatea curenta si verificam daca avem legatura cu macar un nod din ea,contorizam cautarea cu ajutorul variabilei potrivit
    potrivit = 0
    for nod_comunitate in comunitate:
        if matrix[nod - 1][nod_comunitate - 1] == 1:
            potrivit = 1
    return potrivit


def generare_vecin(comunitati):
    #comunitati-multimea curenta de comunitati
    #pentru comunitatea curenta vom alege random un index al unei comunitati cu ajutorul variabilei nr_comunitate,iar mai apoi tot random un nod din ea
    #alegem random o comunitate noua in care sa il introducem
    #cat timp nu nimerim in aceeasi comunitate si nu este pus nicaieri verificam potrivirea sa in comunitatea noua
    #daca se potriveste il adaugam in noua comunitate si il stergem din aceea curenta
    #verificam cazul special in care nodul sustras este singur in comunitate,atunci pentru a evita sa avem comunitati de tipul listelor vide vom sterge definitiv comunitatea din solutie
    #pentru fiecare extragere verificam daca dupa ce nodul este scos din comunitate nu se rup legaturiile importante si avem in continuare o comunitate
    #generam comunitatiile si noduriile random pentru a avea varietate in solutie
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

