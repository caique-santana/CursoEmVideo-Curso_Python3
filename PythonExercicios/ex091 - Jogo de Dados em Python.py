"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
resultados = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
ordem = {}
for i, n in resultados.items():
    resultados[i] = randint(1, 6)
print('Valores sorteados:')
for i, n in resultados.items():
    print(f'O {i} tirou {n}')
    sleep(1)
print('Ranking dos jogadores:')
