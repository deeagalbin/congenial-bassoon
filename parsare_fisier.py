def read_data():
    #citim noduriile ca data
    #citim matrix-ca legaturi
    data = []
    found = 0
    matrix = []
    fisier = input("introduceti fisierul de intrare:")
    with open(fisier, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(" ")
            if line[0].isdigit() and found == 0:
                data.append(int(line[0]))
            elif line[0].isdigit() and found == 1:
                legatura = list()
                legatura.append(int(line[0]))
                legatura.append(int(line[1]))
                matrix.append(legatura)
            else:
                found = 1
    return data, matrix


data, legatura = read_data()


# print(legatura)
# print(data)

def graf(data, legaturi):
    #data-noduriile
    #legaturi-legaturiile dintre noduri
    #returnam un o lista de liste care are ca indice nodul-1 si ca elemente in ea toate noduriile cu care acesta are legaturi
    graf = []
    lista_legatura = []
    for nod in data:
        for k in legaturi:
            if k[0] == nod:
                lista_legatura.append(k[1])
            elif k[1] == nod:
                lista_legatura.append(k[0])
        graf.append(lista_legatura)
        lista_legatura = []
    return graf


def adjencecy_matrix(data, legatura):
    #construim matricea de adiacenta
    #data-noduriile
    #legatura-legaturiile dintre noduri
    #indicii in matrice pornesc de la zero de aceea conditia ca 2 noduri sa aiba legatura:nod1,nod2 e ca matrix[nod1-][nod2-1] sa fie 1
    #matricea construita este simetrica fata de diagonala principala(care va fi 0)
    n = len(data)
    matrix = [[0 for i in range(n)] for j in range(n)]
    for k in legatura:
        # print(str(k[0])+" "+str(k[1]))
        matrix[k[0] - 1][k[1] - 1] = 1
        matrix[k[1] - 1][k[0] - 1] = 1
    # print(matrix[1:n])  # ca sa nu afiseze prima linie,iar noduriile sa inceapa cu 1
    return matrix


matrix = adjencecy_matrix(data, legatura)
