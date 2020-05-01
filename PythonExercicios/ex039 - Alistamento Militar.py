""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
se é a hora de se alistar.
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
# Meu
from datetime import date
tempo = date.today().year
nascimento = int(input('Qual o seu ano de nascimento ? '))
sexo = int(input('''Qual o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino
Digite a opção escolhida: '''))
idade = tempo - nascimento
if sexo == 1:
    if idade < 18:
        print('Você está com {} anos e ainda irá se alistar, \033[1;33mfalta {} anos\033[m para fazer o alistamento'.format(idade, 18 - idade))
    elif idade == 18:
        print('Você está com 18 anos, \033[1;32mestá na hora de se alistar\033[m.')
    else:
        print('Você está com {} anos e o prazo pro seu alistamento \033[1m\033[4;31mpassou já faz(em) {} anos\033[m.'.format(idade, idade - 18))
elif sexo == 2:
    print('O alistamento não é obrigatório para você.')
else:
    print('Opção inválida!')

# Gustavo Guanabara
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
