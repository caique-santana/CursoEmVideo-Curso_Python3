""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
se é a hora de se alistar.
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
# Meu
from datetime import date
tempo = date.today().year
nascimento = int(input('Qual o seu ano de nascimento ? '))
idade = tempo - nascimento
if idade < 18:
    print('Você ainda irá se alistar, \033[1;33mfalta {} anos\033[m para fazer o alistamento'.format(18 - idade))
elif idade == 18:
    print('Você está com 18 anos, \033[1;32mestá na hora de se alistar\033[m.')
else:
    print('O prazo pro seu alistamento \033[1m\033[4;31mpassou já faz(em) {} anos\033[m.'.format(idade - 18))
