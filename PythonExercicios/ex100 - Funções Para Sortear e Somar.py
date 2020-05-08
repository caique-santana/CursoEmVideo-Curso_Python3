"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteio():
    lista = list()
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[c]} ', end='')
        sleep(0.5)
    print('PRONTO!')
    return lista


def somaPar(num):
    s = 0
    for c in num:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {num}, temos {s}')


numero = sorteio()
somaPar(numero)
