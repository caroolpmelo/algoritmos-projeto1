###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Fulano de Tal
# Email:	fdt@cin.ufpe.br
# Data:		2018-03-01
#
# Descricao:  A descricao deve fornecer uma explicacao sucinta do algoritmo (problema)
#				que esta sendo implementado neste arquivo.
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Fulano de Tal
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
   return numpy.random.randint(-MAX,MAX, size=tam)

# Voce deve implementar essa funcao
def conta_somas(vetor):
	pass

def main():
	'''
	Contem os comandos em Python referentes `a implementacao do algoritmo
	'''
	seeds = [11,7,13,19,5189]
	tam = [50,100,250,500,1000]
	for i,seed in enumerate(seeds):
	   numpy.random.seed(seed)
	   vetor = gera_seq_aleatoria(tam[i])
	   cron = Cronometro()
	   total = conta_somas(vetor)
	   print("Tempo gasto com {0} elementos foi {1} segundos".format(tam[i],cron.tempo_gasto()))
	   del vetor
	   del cron


if __name__ == '__main__':
	main()