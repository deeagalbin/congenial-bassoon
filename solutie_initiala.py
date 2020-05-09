from parsare_fisier import *

visited = []
'''
In acest modul generam solutia generala,generare care se realizeaza in jurul unui nod
'''

def find_community(root_graf, graf_comunitati, visited):
    #root_graf-nodul de la care pornim
    #graf-comunitati-graful initial
    #visited-o lista in care punem toate noduriile deja aflate in comunitate pentru a nu ne repeta
    community = [root_graf]
    visited.append(root_graf)
    nod_graf = root_graf
    for child in graf_comunitati[nod_graf - 1]:
        if child not in visited:
            community.append(child)
            visited.append(child)
    return community


'''def adaugare_la_alta_comunitate(comunity, communities):
    nod = comunity[0]
    gasit = 0
    for comunitate in communities:
        for nod_comunitate in comunitate:
            if gasit == 0:
                if nod in graf[nod_comunitate - 1]:
                    comunitate.append(nod)
                    visited.append(nod)
                    gasit = 1
            else:
                break'''


def communities_graph(graf_comunitati, data):
    #graf_comunitati=graful construit in citirea datelor care este o lista de liste avand ca si indice nodul iar ca elemente in lista toate noduriile de care acesta se leaga
    #data=noduriile noastre
    #cosntruim inceand de la primul nod din comunitate un grup de noduri in mici comunitati
    #returneaza solutia initiala 
    communities = []
    for nod in data:
        if nod not in visited:
            community = find_community(nod, graf_comunitati, visited)
            # functie care verifica daca comunitatea are macar 2 lemente
            # dc nu are 2 elemente, il cuplam cu alta comunitate unde gasim
            #if len(community) >= 2:
            communities.append(community)
            #else:
             #   adaugare_la_alta_comunitate(community, communities)
    return communities


#communities = communities_graph(graf, data)
