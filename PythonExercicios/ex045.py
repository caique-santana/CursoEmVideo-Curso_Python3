# Crie um programa que faça o computador jogar Jokenpô com você.
# Meu
from random import choice
print('\033[33m-=-\033[m'*28)
print('\033[1;34mVamos jogar Jokenpô ? Eu já escolhi o meu escolha o seu e vamos ver quem ganha!\033[m')
print('\033[33m-=-\033[m'*28)
comp = ['Pedra', 'Papel', 'Tesoura']
resultado = choice(comp)
jogador = str(input('Escolha um número: Pedra, Papel ou Tesoura ')).capitalize()
if jogador == 'Pedra':
    if resultado == 'Pedra':
        print('EMPATE!\nO dois escolheram Pedra.')
    elif resultado == 'Papel':
        print('PERDEU!\nO computador escolheu {} e você Pedra.'.format(resultado))
    else:
        print('GANHOU!\nO computador escolheu {} e você Pedra.'.format(resultado))
elif jogador == 'Papel':
    if resultado == 'Pedra':
        print('GANHOU!\nO computador escolheu {} e você Papel.'.format(resultado))
    elif resultado == 'Papel':
        print('EMPATE!\nOs dois escolheram Papel.'.format(resultado))
    else:
        print('PERDEU!\nO computador escolheu {} e você Papel.'.format(resultado))
elif jogador == 'Pedra':
    if resultado == 'Pedra':
        print('PERDEU!\nO computador escolheu {} e você Tesoura.'.format(resultado))
    elif resultado == 'Papel':
        print('GANHOU!\nO computador escolheu {} e você Tesoura.'.format(resultado))
    else:
        print('EMPATE!\nOs dois escolheram Tesoura.')
else:
    print('Opção inválida!')

# Gustavo Guanabara
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
