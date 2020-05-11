from random import randint

from conexitate import conex
from parsare_fisier import matrix


# nod-nodul pentru care verificam potrivirea
# comunitate-comunitatea in care incercam sa il introducem
# parcurgem comunitatea curenta si verificam daca avem legatura cu macar un nod din ea,contorizam cautarea cu ajutorul variabilei
def potrivit_comunitate(nod, comunitate):
    potrivit = 0
    for nod_comunitate in comunitate:
        if matrix[nod - 1][nod_comunitate - 1] == 1:
            potrivit = 1
    return potrivit

#pentru nodul nod verificam cate legaturi are cu comunitatea comunitate
#input:nod-nodul curent,comunitate-comunitatea in care dorim sa adaugam
#nr_legaturi-numarul de legaturi al nodului cu comunitatea
def legaturi_in_comunitate(nod, comunitate):
    nr_legaturi = 0
    for element in comunitate:
        if matrix[element - 1][nod - 1] == 1:
            nr_legaturi += 1
    return nr_legaturi


#nod-un nod pe care vrem sa il schimbam
#comunitati-listele cu comunitatiile prezente
#output:indexul comunitatii cu care are cele mai multe legaturi
def comunitate_noua(nod, comunitati):
    max_legaturi = legaturi_in_comunitate(nod, comunitati[0])
    index_comunitate_noua = 0
    i = 1
    while i < len(comunitati):
        if legaturi_in_comunitate(nod, comunitati[i]) > max_legaturi:
            index_comunitate_noua = i
            max_legaturi = legaturi_in_comunitate(nod, comunitati[i])
        i = i + 1
    return index_comunitate_noua

# comunitati-multimea curenta de comunitati
# pentru comunitatea curenta vom alege random un index al unei comunitati cu ajutorul variabilei nr_comunitate,iar mai apoi tot random un nod din ea
# alegem determinist o comunitate noua in care sa il introducem(cea cu care are cele mai multe legaturi)
# cat timp nu este pus deja in comunitate il adaugam la o comunitate potrivita
# daca se potriveste il adaugam in noua comunitate si il stergem din aceea curenta
# verificam cazul special in care nodul sustras este singur in comunitate,atunci pentru a evita sa avem comunitati de tipul listelor vide vom sterge definitiv comunitatea din solutie
# pentru fiecare extragere verificam daca dupa ce nodul este scos din comunitate nu se rup legaturiile importante si avem in continuare o comunitate
# generam comunitatiile si noduriile random pentru a avea varietate in solutie
def generare_vecin(comunitati):
    lungime_comunitati = len(comunitati)
    nr_comunitate = randint(0, lungime_comunitati - 1)
    index_nod = randint(0, len(comunitati[nr_comunitate]) - 1)
    nod = comunitati[nr_comunitate][index_nod]
    pus_in_comunitate = 0
    nr_comunitate_noua = comunitate_noua(nod, comunitati)
    while pus_in_comunitate == 0:
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
