# RA 260240

# Se necessario importe suas bibliotecas aqui
from sys import stdin

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

    def eh_maior_ou_igual(self, outra_data):
        if self._ano < outra_data.ano:
            return False
        if self._mes < outra_data.mes:
            return False
        if self._dia < outra_data.dia:
            return False
        return True

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

# Aqui em baixo fica a sua solucao

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

voos = []
passagem_props = {
    'num': '',
    'cods_aeroportos': '',
    'data': '',
    'preco': '',
}

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

def registrar():
    for p in passagem_props.keys():
        valor = input().strip()
        passagem_props.update({p:valor})

    num = int(passagem_props.get('num'))
    cod_origem = passagem_props.get('cods_aeroportos').split()[0]
    cod_destino = passagem_props.get('cods_aeroportos').split()[1]
    dia, mes, ano = formatar_data(passagem_props.get('data'))
    data = Data(dia, mes, ano)
    preco = float(passagem_props.get('preco'))

    voo = Voo(num, cod_origem, cod_destino, data, preco)
    voos.append(voo)

def alterar(num_voo, valor):
    voo = encontrar_voo(int(num_voo))
    preco_antes = voo.preco
    voo.preco = float(valor)
    print(f"{num_voo} valor alterado de {preco_antes} para {voo.preco}")

def cancelar(num_voo):
    voo = encontrar_voo(int(num_voo))
    voos.pop(voos.index(voo))

for linha in stdin:
    linha = linha.strip()
    if linha == 'registrar':
        registrar()

    elif linha == 'alterar':
        num_voo, valor = input().strip().split()
        alterar(num_voo, valor)

    elif linha == 'cancelar':
        num_voo = input().strip()
        cancelar(num_voo)

    elif linha == 'planejar':
        jarzinho_aeroporto = input().strip()
        data_inicio_ferias, data_fim_ferias = input().strip().split()
        dia, mes, ano = formatar_data(data_inicio_ferias)
        data_inicio_ferias = Data(dia, mes, ano)
        dia, mes, ano = formatar_data(data_fim_ferias)
        data_fim_ferias = Data(dia, mes, ano)
        
        dia_limite = data_fim_ferias.dia - 3
        mes_limite = data_fim_ferias.mes
        ano_limite = data_fim_ferias.ano
        
        if dia_limite <= 0:
            mes_limite = data_fim_ferias.mes - 1
            if mes_limite == 0:
                mes_limite = 12
                ano_limite = data_fim_ferias.ano -1
            dia_limite = dias_por_mes.get(mes_limite) - dia_limite
        
        data_limite_passagem = Data(dia_limite,mes_limite,ano_limite)
        
        voos_com_aeroporto_do_jarzinho = encontrar_voos_com_aeroporto_de_origem(jarzinho_aeroporto)
        melhor_voo = voos_com_aeroporto_do_jarzinho[0]
        
        for v in voos_com_aeroporto_do_jarzinho:
            if v.data.eh_maior_ou_igual(data_inicio_ferias) == False and v.data.eh_maior_ou_igual(data_limite_passagem) == True:
                continue

            if v.preco < melhor_voo.preco:
                melhor_voo = v
        
        print(melhor_voo.numero)
        print(melhor_voo.numero)


