from parsare_fisier import *


# Calculeaza gradului unui nod
# Input: nodul
# Output: gradul nodului (numarul muchiilor incidente care trec prin nod)
def node_degree(nod):
    degree = 0
    for i in range(len(data)):
        if matrix[nod - 1][i] == 1:
            degree += 1
    return degree


# Valoare functiei Kronecker indica daca 2 noduri sunt in aceeasi comunitate sau nu
# Input: lista de comunitati, doua noduri (i si j)
# Output: False - nodurile nu sunt in aceeasi comunitate; True - nodurile sunt in aceeasi comunitate
def Kronecker_function(comunitati, node_i, node_j):
    community_i = None
    community_j = None
    ok = 0
    for k in range(len(comunitati)):
        if node_i in comunitati[k]:
            community_i = k
        if node_j in comunitati[k]:
            community_j = k
    if community_i == community_j:
        ok = 1
    return ok


# Formula de calul a modularitatii - Formula (10) din art. de referinta
# Input: comunitatile
# Outpu: valoara modularitatii
def eval_solutie(comunitati):
    modularity = 0
    edges = len(legatura)
    sum = 0
    for i in range(len(data)):
        for j in range(len(data)):
            sum = sum + (matrix[i][j] - ((node_degree(i + 1) * node_degree(j + 1)) / (2 * edges))) * \
                  Kronecker_function(comunitati, i + 1, j + 1)
    modularity = (1 / (2 * edges)) * sum
    return modularity
   
