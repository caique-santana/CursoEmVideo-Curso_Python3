"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
# Meu
from random import randint
comp = randint(0, 10)
print('\033[1;33m=*=\033[m'*25)
print('\033[1;34mVocê é capaz de descobrir o número que o computador escolheu entre 0 e 10?\033[m')
print('\033[1;33m=*=\033[m'*25)
jogador = int(input('Escolha um número: '))
cont = 1
while jogador != comp:
    if jogador > comp:
        print('\033[1m\033[4;31mMenor\033[m ...')
    else:
        print('\033[1m\033[4;32mMaior\033[m...')
    num = int(input('Tente outro número: '))
    jogador = num
    cont += 1
print('\033[1;36;42mAcertou, Parabéns!\033[m\nForam necessários \033[1;33m{}\033[m tentativas para você acertar.'.format(cont))

# Gustavo Guanabara
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
