"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
Fazer usando WHILE e depois FOR"""
# Meu
from math import factorial
continuar = 'S'
while continuar != 'N':
    num = float(input('Digite um número para saber seu fatorial: '))
    print(factorial(num))
    continuar = str(input('Quer continuar? [S/N] ')).upper()

num = int(input('Digite um número: '))
cont = num
f = 1
for cont in range(cont, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
print('{}'.format(f))

# Gustavo Guanabara
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))

