matriz = []
caminho = []

def encontrar_caminho(matriz, coord_inicio, visitado=None):
    if visitado == None:
        visitado = set()

    caminho = []
    sem_saida = True
    x, y = coord_inicio

    visitado.add((x, y))

    if matriz[x][y] == ' ':
        caminho += [coord_inicio]
    elif matriz[x][y] == 'S':
        return caminho + [coord_inicio]

    if x < len(matriz) - 1:
        sem_saida = False
        nova_coord = (x + 1, y)
        if nova_coord not in visitado and (matriz[nova_coord[0]][nova_coord[1]] == ' ' or matriz[nova_coord[0]][nova_coord[1]] == 'S'):
            novo_caminho = encontrar_caminho(matriz, nova_coord, visitado)
            if novo_caminho != []:
                return [coord_inicio] + novo_caminho
            
    if y < len(matriz[0]) - 1:
        sem_saida = False
        nova_coord = (x, y + 1)
        if nova_coord not in visitado and (matriz[nova_coord[0]][nova_coord[1]] == ' ' or matriz[nova_coord[0]][nova_coord[1]] == 'S'):
            novo_caminho = encontrar_caminho(matriz, nova_coord, visitado)
            if novo_caminho != []:
                return [coord_inicio] + novo_caminho

    if y > 0:
        sem_saida = False
        nova_coord = (x, y - 1)
        if nova_coord not in visitado and (matriz[nova_coord[0]][nova_coord[1]] == ' ' or matriz[nova_coord[0]][nova_coord[1]] == 'S'):
            novo_caminho = encontrar_caminho(matriz, nova_coord, visitado)
            if novo_caminho != []:
                return [coord_inicio] + novo_caminho


    if x > 0:
        sem_saida = False
        nova_coord = (x - 1, y)
        if nova_coord not in visitado and (matriz[nova_coord[0]][nova_coord[1]] == ' ' or matriz[nova_coord[0]][nova_coord[1]] == 'S'):
            novo_caminho = encontrar_caminho(matriz, nova_coord, visitado)
            if novo_caminho != []:
                return [coord_inicio] + novo_caminho

    if sem_saida:
        return []

    return caminho
while True:
    linha = list(input().strip())
    matriz.append(linha)

    for l in range(len(matriz)):
        for i in range(len(matriz[l])):
            if matriz[l][i] == 'E':
                coord_inicio = (l, i)
                break

    caminho = encontrar_caminho(matriz, coord_inicio)
    for coord in caminho:
        print(coord)
