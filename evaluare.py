from parsare_fisier import *


def node_degree(nod):
    degree = 0
    for i in range(len(data)):
        if matrix[nod - 1][i] == 1:
            degree += 1
    return degree


# print("node " + str(node_degree(2)))
# print(matrix[1][0:]) #ca sa pot numara pt test cate grade are


def Kronecker_function(comunitati, node_i, node_j):
    # community_i, community_j - comunitatile nodurilor i si j
    community_i = None
    community_j = None
    ok = False  # pp ca nu sunt in aceeasi comunitate
    for k in range(len(comunitati)):
        if node_i in comunitati[k]:
            community_i = k
        if node_j in comunitati[k]:
            community_j = k
    if community_i == community_j:
        ok = True  # nodurile sunt in aceeasi comunitate
    return ok


#print(comunitati)
#print(Kronecker_function(2, 31))

#The modularity can be either positive or negative,
# with positive values indicating the possible presence of community structure.
def eval_solutie(comunitati):
    modularity = 0
    double_edges = 2*len(legatura)
    sum = 0
    for i in range(len(data)):
        for j in range(len(data)):
            sum = sum + (matrix[i][j] - ((node_degree(i) * node_degree(j))/double_edges)) * Kronecker_function(comunitati,i, j)
    modularity = (1 / double_edges) * sum
    return modularity


#print(eval_solutie(comunitati))
