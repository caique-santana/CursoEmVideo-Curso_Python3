"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""
# Meu
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num > 1 and num % c == 0:
        cont += 1
if cont == 2:
    print('O número {} foi divisível {} vezes\nE por isso ele É PRIMO!'.format(num, cont))
else:
    print('O númeor {} foi divisível {} vezes\nE por isso ele NÃO É PRIMO!'.format(num, cont))

# Gustavo Guanabara
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')