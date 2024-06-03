def encontrar_combinacoes(n):
    def backtrack(combinacao_atual, inicio, n, resultados):
        if n == 0:
            resultados.append(combinacao_atual[:])
            return
        for i in range(inicio, n + 1):
            combinacao_atual.append(i)
            backtrack(combinacao_atual, i, n - i, resultados)
            combinacao_atual.pop()

    resultados = []
    backtrack([], 1, n, resultados)
    return resultados

def formatar_combinacoes(combinacoes, n):
    combinacoes_formatadas = []
    for combinacao in combinacoes:
        comb_str = '+'.join(map(str, combinacao)) + '=' + str(n)
        combinacoes_formatadas.append(comb_str)
    return combinacoes_formatadas

n = int(input())

combinacoes = encontrar_combinacoes(n)

combinacoes_formatadas = formatar_combinacoes(combinacoes, n)

for comb in combinacoes_formatadas:
    print(comb)
