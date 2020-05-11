from parsare_fisier import *

visited = []


# root_graf-nodul de la care pornim
# graf-comunitati-graful initial
# visited-o lista in care punem toate noduriile deja aflate in comunitate pentru a nu ne repeta
def find_community(root_graf, graf_comunitati, visited):
    community = [root_graf]
    visited.append(root_graf)
    nod_graf = root_graf
    for child in graf_comunitati[nod_graf - 1]:
        if child not in visited:
            community.append(child)
            visited.append(child)
    return community


# graf_comunitati=graful construit in citirea datelor care este o lista de liste avand ca si indice nodul iar ca elemente in lista toate noduriile de care acesta se leaga
# data=noduriile noastre
# cosntruim inceand de la primul nod din comunitate un grup de noduri in mici comunitati
# returneaza solutia initiala
def communities_graph(graf_comunitati, data):
    communities = []
    for nod in data:
        if nod not in visited:
            community = find_community(nod, graf_comunitati, visited)
            communities.append(community)
    return communities

# communities = communities_graph(graf, data)
