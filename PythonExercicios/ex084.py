"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
dados = list()
pessoas = list()
cont = pessado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if cont == 0:
        pessado = leve = dados[1]
    else:
        if dados[1] > pessado:
            pessado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    cont += 1
    dados.clear()
    continuar = str(input('Quer continuar ? [S/N] '))
    if continuar in 'Nn':
        break
print('-=-' * 18)
print(f'Foram cadastrados {cont} pessoas.')
print(f'O maior peso foi de {pessado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pessado:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {leve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]} ', end='')
