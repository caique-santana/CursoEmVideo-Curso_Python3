'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número:6.127 | O número 6.127 tem a parte Inteira 6.'''
from math import trunc
real = float(input('Digite um número real: '))
print('O número {} tem a porção inteira {}'.format(real, trunc(real)))

# Gustavo Guanabara
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))