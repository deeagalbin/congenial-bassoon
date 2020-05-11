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

#calculeaza gardul unui nod
def node_degree(nod):
    degree = 0
    for i in range(len(data)):
        if matrix[nod - 1][i] == 1:
            degree += 1
    return degree

#o noua abordare a solutiei initiale
#alegem aleator un numar de  comunitati
#adaugam fiecare nod in comunitatea potrivita
#alegem random o comunitatea in care sa punem nodul,astfel incata vem mereu varietate in solutia initiala
#daca raman noduri nepotrivite mai parcurgem o data comunitatiile si le adaugam din nou(acest lucru fiind posibil datorita ordinii noduriilor)
def rafinare_solutie_initiala():
    min_nr_comunitati = int(len(data) / 10)
    max_nr_comunitati = int(len(data) / 5)
    nr_exact = randint(min_nr_comunitati, max_nr_comunitati)
    comunitati = [[] for i in range(nr_exact)]
    nepotrivire_initial = []
    for nod in data:
        nr_comunitate_nod = randint(0, nr_exact - 1)
        pus_in_comunitate = 0
        while pus_in_comunitate == 0:
            if len(comunitati[nr_comunitate_nod]) == 0:
                comunitati[nr_comunitate_nod].append(nod)
                pus_in_comunitate = 1
            else:
                if potrivit_comunitate(nod, comunitati[nr_comunitate_nod]) == 1 and \
                        len(comunitati[nr_comunitate_nod]) < int(len(data) / 4):
                    comunitati[nr_comunitate_nod].append(nod)
                    pus_in_comunitate = 1
                else:
                    nepotrivire_initial.append(nod)
                    pus_in_comunitate = 1
    if len(nepotrivire_initial) != 0:
        while (len(nepotrivire_initial) != 0):
            i = 0
            while i < len(nepotrivire_initial):
                lungime = len(comunitati)
                nr_comunitate_nod = randint(0, lungime - 1)
                pus_in_comunitate = 0
                while pus_in_comunitate == 0:
                    if potrivit_comunitate(nepotrivire_initial[i], comunitati[nr_comunitate_nod]) == 1:
                        if (len(comunitati[nr_comunitate_nod]) < len(data) / 3):
                            comunitati[nr_comunitate_nod].append(nepotrivire_initial[i])
                            pus_in_comunitate = 1
                            nepotrivire_initial.remove(nepotrivire_initial[i])
                            i += 1
                        else:
                            comunitati[nr_comunitate_nod].append(nepotrivire_initial[i])
                            nepotrivire_initial.remove(nepotrivire_initial[i])
                            pus_in_comunitate = 1
                            lungime += 1
                            i += 1
                    else:
                        i = i + 1
                        pus_in_comunitate = 1
    return comunitati

# communities = communities_graph(graf, data)
