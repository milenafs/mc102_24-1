lista_num = list(map(int, input().split()))

def sort(lista):
    num = lista[0]

    if len(lista) == 1:
        return [num]

    lista_outros_num = sort(lista[1:])

    if num > lista_outros_num[-1]:
        return lista_outros_num + [num]
    
    elif num < lista_outros_num[0]:
        return [num] + lista_outros_num
    
    lista_outros_num = [num] + lista_outros_num
    menor_num_indice = 0
    for i in range(len(lista_outros_num)):
        if lista_outros_num[menor_num_indice] > lista_outros_num[i]:
            lista_outros_num[menor_num_indice], lista_outros_num[i] =  lista_outros_num[i], lista_outros_num[menor_num_indice]
            menor_num_indice = i
    
    return lista_outros_num

print(sort(lista_num))