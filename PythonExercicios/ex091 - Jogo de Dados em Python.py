"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
# Caique Santana
from random import randint
from time import sleep
resultados = {'jogador-1': 0, 'jogador-2': 0, 'jogador-3': 0, 'jogador-4': 0}
ordem = {}
for i, n in resultados.items():
    resultados[i] = randint(1, 6)
print('Valores sorteados:')
for i, n in resultados.items():
    print(f'O {i} tirou {n}')
    sleep(1)

# Gustavo Guanabara
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)
