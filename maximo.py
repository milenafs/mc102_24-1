lista_num = list(map(int, input().split()))

def get_maior_num(lista):
    
    max = lista[0]

    if len(lista) == 1:
        return max
    
    aux = get_maior_num(lista[1:]) 
    if aux > max:
        max = aux

    return max

print(get_maior_num(lista_num))

