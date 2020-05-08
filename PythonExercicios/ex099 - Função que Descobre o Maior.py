"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
# Caique Santana
from time import sleep


def maior(*num):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
        if c > maior:
            maior = c
    if len(num) > 1:
        print(f'Foram informados {len(num)} valores ao todo.')
    else:
        print(f'Foi informado {len(num)} valor ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# Gustavo Guanabara
from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram imforados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
