"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
# Caique Santana
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

# Gustavo Guanabara
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Pedo: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
