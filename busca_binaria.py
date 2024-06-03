lista_num = list(map(int, input().split()))
i = int(input())

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return busca_binaria(lista[meio+1:], valor) + meio + 1
    elif lista[meio] > valor:
        return busca_binaria(lista[inicio:meio], valor)
    
    return -1 

print(busca_binaria(lista_num, i))