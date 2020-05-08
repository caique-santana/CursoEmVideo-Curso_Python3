"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada."""
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim or passo < 0:
        fim -= passo
        passo *= -1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
