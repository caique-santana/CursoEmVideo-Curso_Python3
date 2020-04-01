# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# Meu
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('O ano {} \033[4;34mé Bissexto\033[m!'.format(ano))
else:
    print('O ano {} \033[4;31mnão é Bissexto\033[m!'.format(ano))

# Gustavo Guananara
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
