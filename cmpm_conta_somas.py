###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Carolina Maria de Paiva Melo
# Email:	cmpm@cin.ufpe.br
# Data:		2018-03-11
#
# Descricao:  O algoritmo implementado nesse arquivo recebe um vetor e, a partir dele,
#             calcula quantas triplas do mesmo somam a zero, exibindo seu tempo de execucao.
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Carolina Maria de Paiva Melo
#
###############################################################################

import sys
from time import perf_counter
import numpy

MAX = 999999

class Cronometro:
    ''' Cronometra tempo gasto desde a criacao ate a chamada do metodo
       tempo_gasto
   '''
    def __init__(self):
        self.__criacao = perf_counter()
    def tempo_gasto(self):
        return perf_counter() - self.__criacao

def gera_seq_aleatoria(tam):
    return numpy.random.randint(-MAX, MAX, size=tam)

# Funcao implementada:
def conta_somas(vetor):
    total = 0
    tamanho = len(vetor)

    # Objetivo: receber o vetor e iterar sobre as posicoes do mesmo.
    # Fazer combinacoes entre essas posicoes e junta-las de tres em tres,
    # de modo que a soma entre essas tres posicoes resulte em zero.
    # Caso resulte em zero, soma +1 ao valor total, para contabilizar as triplas
    # que satisfacam essa condicao.

    a = 0 # contador inicial
    while (a < tamanho): # primeiro elemento da tripla
        elem1 = vetor[a]

        b = a + 1
        while (b < tamanho): # segundo elemento da tripla
            elem2 = vetor[b]

            c = b + 1
            while (c < tamanho): # terceiro elemento da tripla
                elem3 = vetor[c]

                # soma é feita aqui pois a ultima tripla será formada quando
                # c chegar ao fim do array
                soma = elem1+elem2+elem3
                if soma == 0:
                    #total++
                    total += 1
                #c++
                c += 1
            #b++
            b +=1
        #a++
        a += 1
    return total

def main():
    '''
	Contem os comandos em Python referentes `a implementacao do algoritmo
	'''
    seeds = [11, 7, 13, 19, 5189]
    tam = [50, 100, 250, 500, 1000]
    for i, seed in enumerate(seeds):
        numpy.random.seed(seed)
        vetor = gera_seq_aleatoria(tam[i])
        cron = Cronometro()
        total = conta_somas(vetor)
        print("Tempo gasto com {0} elementos foi {1} segundos".format(tam[i], cron.tempo_gasto()))
        # 'Resultado: ' se refere as triplas que somadas são zero
        print("Resultado: ", total)
        del vetor
        del cron

if __name__ == '__main__':
    main()
