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

def encontrar_melhor_voo(array_voos, data_min, data_max):
    melhor_voo = array_voos[0]

    for v in array_voos:
        if v.data.eh_maior(data_max) or v.data.eh_menor(data_min):
            continue

        if v.preco < melhor_voo.preco:
            melhor_voo = v

    return melhor_voo

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
        data_limite_passagem_ida = data_fim_ferias
        data_limite_passagem_ida.somar_subtrair_dias(-4)
        
        # dia_limite_ida = data_fim_ferias.dia - 3
        # mes_limite_ida = data_fim_ferias.mes
        # ano_limite_ida = data_fim_ferias.ano
        
        # if dia_limite_ida <= 0:
        #     mes_limite_ida = data_fim_ferias.mes - 1
        #     if mes_limite_ida == 0:
        #         mes_limite_ida = 12
        #         ano_limite_ida = data_fim_ferias.ano -1
        #     dia_limite_ida = dias_por_mes.get(mes_limite_ida) - dia_limite_ida
        
        # data_limite_passagem_ida = Data(dia_limite_ida,mes_limite_ida,ano_limite_ida)
        
        voos_com_aeroporto_do_jarzinho = encontrar_voos_com_aeroporto_de_origem(jarzinho_aeroporto)

        melhor_voo_ida = encontrar_melhor_voo(voos_com_aeroporto_do_jarzinho, data_inicio_ferias, data_limite_passagem_ida)

        # melhor_voo_ida = voos_com_aeroporto_do_jarzinho[0]
        
        # for v in voos_com_aeroporto_do_jarzinho:
        #     if v.data.eh_maior_ou_igual(data_inicio_ferias) == False and v.data.eh_maior_ou_igual(data_limite_passagem_ida) == True:
        #         continue

        #     if v.preco < melhor_voo_ida.preco:
        #         melhor_voo_ida = v

        data_limite_passagem_volta = data_limite_passagem_ida
        data_limite_passagem_volta.somar_subtrair_dias(4)
        
        voos_retorno_viajem = encontrar_voos_com_aeroporto_de_origem(melhor_voo_ida.aeroport_destino_cod)

        melhor_voo_volta = encontrar_melhor_voo(voos_retorno_viajem, data_limite_passagem_volta, data_fim_ferias)
        # melhor_voo_volta = voos_retorno_viajem[0]

        # for v in voos_retorno_viajem:
        #     if v.data.eh_maior_ou_igual(data_inicio_ferias) == False and v.data.eh_maior_ou_igual(data_limite_passagem_volta) == True:
        #         continue

        #     if v.preco < melhor_voo_volta.preco:
        #         melhor_voo_volta = v
        
        print(melhor_voo_ida.numero)
        print(melhor_voo_volta.numero)


