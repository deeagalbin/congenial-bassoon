from parsare_fisier import *

noduri_totale = len(data)


def conex(comunitate):
    #prin aceasta functie stabilim daca odata ce luam un nod dintr-o comunitate avem un graf conex
    #adica nodurile ramase vor constitui in continuare o comunitate
    gasit = 1
    n = len(comunitate)
    vizitat = [0 for i in range(noduri_totale)]
    vizitat_update = verifica_legaturi(comunitate, vizitat)
    for i in range(n):
        if vizitat_update[comunitate[i] - 1] == 0:
            gasit = 0
    return gasit


def verifica_legaturi(comunitate, vizitat):
    #aici vom parcurge fiecare nod din comunitate pentru a stabili daca avem legaturi intre ele sau avem si noduri izolate
    for i in range(0, len(comunitate)):
        for nod in comunitate:
            if matrix[comunitate[i] - 1][nod - 1] == 1 and vizitat[nod - 1] == 0:
                vizitat[nod - 1] = 1
    return vizitat

# print(communities[3])
# vec = [0 for i in range(noduri_totale)]
# vizit = verifica_legaturi(communities[1], vec)
# print(vizit)
# conexitate = conex(communities[1])
