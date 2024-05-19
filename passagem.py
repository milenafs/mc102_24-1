# RA 260240

from sys import stdin

"""
    Classe Data:
        propriedades:
            - dia (int)
            - mes (int)
            - ano (int)
        métodos:
            - eh_maior(data) -> boolean
                compara se a instância atual é maior do que o objeto Data passado nos parâmetros
            - eh_menor(data) -> boolean
                compara se a instância atual é menor do que o objeto Data passado nos parâmetros
            - eh_igual(data) -> boolean
                compara se a instância atual é igual ao objeto Data passado nos parâmetros
            - somar_subtrair_dias(dias)
                soma o número de dias passado no parâmetro ao objeto, fazendo alterações no mês e ano caso necessárias
"""
class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    @property
    def dia(self):
        return self._dia
    
    @dia.setter
    def dia(self, dia):
        self._dia = dia
    
    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self, mes):
        self._mes = mes
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    def eh_maior(self, outra_data):
        if self._ano < outra_data.ano:
            return False
        if self._mes < outra_data.mes:
            return False
        if self._dia <= outra_data.dia:
            return False
        return True
    
    def eh_menor(self, outra_data):
        if self._ano > outra_data.ano:
            return False
        if self._mes > outra_data.mes:
            return False
        if self._dia >= outra_data.dia:
            return False
        return True
    
    def eh_igual(self, outra_data):
        if self._ano != outra_data.ano or self._mes != outra_data.mes or self._dia != outra_data.dia:
            return False
        return True

    def somar_subtrair_dias(self, dias_a_somar):
        dias_por_mes = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        dia = self._dia + dias_a_somar
        mes = self._mes
        ano = self._ano
        
        if dia <= 0:
            mes = self._mes - 1
            if mes == 0:
                mes = 12
                ano = self._ano -1
            dia = dias_por_mes.get(mes) - dia
        
        self._dia = dia
        self._mes = mes
        self._ano = ano

"""
    Classe Voo:
        propriedades:
            - numero (int)
            - aeroport_origem_cod (string)
            - aeroport_destino_cod (string)
            - data (Data)
            - preco (float)
"""
class Voo:
    def __init__(self, numero, aeroport_origem_cod, aeroport_destino_cod, data, preco):
        self._numero = numero
        self._aeroport_origem_cod = aeroport_origem_cod
        self._aeroport_destino_cod = aeroport_destino_cod
        self._data = data
        self._preco = preco
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def aeroport_origem_cod(self):
        return self._aeroport_origem_cod
    
    @aeroport_origem_cod.setter
    def aeroport_origem_cod(self, aeroport_origem_cod):
        self._aeroport_origem_cod = aeroport_origem_cod

    @property
    def aeroport_destino_cod(self):
        return self._aeroport_destino_cod
    
    @aeroport_destino_cod.setter
    def aeroport_destino_cod(self, aeroport_destino_cod):
        self._aeroport_destino_cod = aeroport_destino_cod

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

# voo é um array de objetos do tipo Voo, que guardará os voos do arquivo de entrada.in
voos = []

# formatar_data(data) recebe um data do tipo string dd/mm/aaaa e retorna [dd, mm, aaaa]
def formatar_data(data):
    d, m, a = map(int,data.split('/'))
    return d,m,a

def encontrar_voo(numero):
    for i in range(len(voos)):
        if voos[i].numero == numero:
            return voos[i]

def encontrar_voos_com_aeroporto_de_origem(codigo):
    res = []
    for i in range(len(voos)):
        if voos[i].aeroport_origem_cod == codigo:
            res.append(voos[i])
    return res

# encontrar_melhor_voo(array_voos, data_min, data_max) retorno o melhor voo encontrado no array passado conferindo se ele está dentro do período desejado e se tem o melhor preço
def encontrar_melhor_voo(array_voos, data_min, data_max):
    melhor_voo = array_voos[0]

    for v in array_voos:
        if v.data.eh_maior(data_max) or v.data.eh_menor(data_min):
            continue

        if v.preco < melhor_voo.preco:
            melhor_voo = v

    return melhor_voo

def registrar_voo():
    passagem_props = {
        'num': '',
        'cods_aeroportos': '',
        'data': '',
        'preco': '',
    }

    # lê cada linha de registro e coloca seu valor no dicionário
    for p in passagem_props.keys():
        valor = input().strip()
        passagem_props.update({p:valor})

    # faz as formatações dos valores do voo necessárias
    num = int(passagem_props.get('num'))
    cod_origem = passagem_props.get('cods_aeroportos').split()[0]
    cod_destino = passagem_props.get('cods_aeroportos').split()[1]
    dia, mes, ano = formatar_data(passagem_props.get('data'))
    data = Data(dia, mes, ano)
    preco = float(passagem_props.get('preco'))

    # cria um novo objeto do tipo Voo e coloca no arrays geral de voos
    voo = Voo(num, cod_origem, cod_destino, data, preco)
    voos.append(voo)

def alterar_preco_voo(num_voo, valor):
    voo = encontrar_voo(int(num_voo))
    preco_antes = voo.preco
    voo.preco = float(valor)
    print(f"{num_voo} valor alterado de {preco_antes} para {voo.preco}")

def cancelar_voo(num_voo):
    voo = encontrar_voo(int(num_voo))
    voos.pop(voos.index(voo))

for linha in stdin:
    linha = linha.strip()

    if linha == 'registrar':
        registrar_voo()

    elif linha == 'alterar':
        num_voo, valor = input().strip().split()
        alterar_preco_voo(num_voo, valor)

    elif linha == 'cancelar':
        num_voo = input().strip()
        cancelar_voo(num_voo)

    elif linha == 'planejar':
        jarzinho_aeroporto = input().strip()
        data_inicio_ferias, data_fim_ferias = input().strip().split()
        
        # formata a data de início de férias
        dia, mes, ano = formatar_data(data_inicio_ferias)
        data_inicio_ferias = Data(dia, mes, ano)
        
        # formata a data de fim de férias
        dia, mes, ano = formatar_data(data_fim_ferias)
        data_fim_ferias = Data(dia, mes, ano)
        
        # data_limite_passagem_ida recebe a data do fim menos 4, que é o período mímino de viajem que jarzinho deseja
        data_limite_passagem_ida = data_fim_ferias
        data_limite_passagem_ida.somar_subtrair_dias(-4)

        # filtra os voos que tem o aeroporto de ida que jarzinho quer, e depois encontra aquele dentro do limite de ida (data_inicio_ferias <= data <= data_limite_passagem_ida) e com o melhor preço
        voos_com_aeroporto_do_jarzinho = encontrar_voos_com_aeroporto_de_origem(jarzinho_aeroporto)
        melhor_voo_ida = encontrar_melhor_voo(voos_com_aeroporto_do_jarzinho, data_inicio_ferias, data_limite_passagem_ida)

        # data_limite_passagem_volta recebe a data que ele ira embarcar mais 4 que é período mínimo da viajem
        data_limite_passagem_volta = data_limite_passagem_ida
        data_limite_passagem_volta.somar_subtrair_dias(4)
        
        # filtra os voos que tem o mesmo aeroporto de ida igual do destino que jarzinho estará viajando, e depois encontra aquele dentro do limite de ida (data_limite_passagem_volta <= data <= data_fim_ferias) e com o melhor preço
        voos_retorno_viajem = encontrar_voos_com_aeroporto_de_origem(melhor_voo_ida.aeroport_destino_cod)
        melhor_voo_volta = encontrar_melhor_voo(voos_retorno_viajem, data_limite_passagem_volta, data_fim_ferias)
        
        print(melhor_voo_ida.numero)
        print(melhor_voo_volta.numero)


