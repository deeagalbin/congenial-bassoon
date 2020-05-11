from parsare_fisier import *

noduri_totale = len(data)


def conex(comunitate):
    #verificam daca intr-o comunitate ramasa avem intr-adevar o comunitate odata cu scoaterea unui nod
    #comunitate=comunitatea ramasa dupa ce scoatem un nod
    #parcurgem comunitatea si utilizam un vector vizitat initializat cu 0,daca avem vreun nod care nu a fost vizitata macar o data,inseamna ca acesta e
    gasit = 1
    n = len(comunitate)
    vizitat = [0 for i in range(noduri_totale)]
    vizitat_update = verifica_legaturi(comunitate, vizitat)
    for i in range(n):
        if vizitat_update[comunitate[i] - 1] == 0:
            gasit = 0
    return gasit


def verifica_legaturi(comunitate, vizitat):
    #comunitate=comunitatea pt care verificam legaturiile
    #vizitat=vectorul de zerouri initializat
    #parcurgem bfs o comunitate si cu ajutorul matricii de adicente prelucram vectorul vizitat care ne va spune daca nodul a fost sau nu parcurs 
    for i in range(0, len(comunitate)):
        for nod in comunitate:
            if matrix[comunitate[i] - 1][nod - 1] == 1 and vizitat[nod - 1] == 0:
                vizitat[nod - 1] = 1
    return vizitat
