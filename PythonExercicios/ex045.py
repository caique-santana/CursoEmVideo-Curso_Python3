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
else:
    if resultado == 'Pedra':
        print('PERDEU!\nO computador escolheu {} e você Tesoura.'.format(resultado))
    elif resultado == 'Papel':
        print('GANHOU!\nO computador escolheu {} e você Tesoura.'.format(resultado))
    else:
        print('EMPATE!\nOs dois escolheram Tesoura.')
