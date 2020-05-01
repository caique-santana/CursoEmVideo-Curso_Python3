'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
# Meu
from random import randint
ncomp = randint(0, 5)
print('\033[1;30mO computador escolheu um número entre 0 e 5, agora é a sua vez\033[m')
nusu = int(input('Tente descobrir o número que o computador escolheu: '))
if nusu == ncomp:
    print('\033[1m\033[4;34mVocê acertou\033[m!')
else:
    print('\033[1m\033[4;31mVocê errou\033[m, o número escolhido foi \033[1;34m{}\033[m.'.format(ncomp))

# Gustavo Guanabara
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
