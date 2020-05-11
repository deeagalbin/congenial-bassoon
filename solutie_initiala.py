from parsare_fisier import *

visited = []


def find_community(root_graf, graf_comunitati, visited):
    community = [root_graf]
    visited.append(root_graf)
    nod_graf = root_graf
    for child in graf_comunitati[nod_graf - 1]:
        if child not in visited:
            community.append(child)
            visited.append(child)
    return community


def communities_graph(graf_comunitati, data):
    communities = []
    for nod in data:
        if nod not in visited:
            community = find_community(nod, graf_comunitati, visited)
            communities.append(community)
    return communities


#communities = communities_graph(graf, data)
