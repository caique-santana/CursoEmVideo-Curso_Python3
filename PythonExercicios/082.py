"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
# Caique Santana
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar [S/N] ? ')).upper()
    if continuar == 'N':
        break
pares = []
impares = []
for i, c in enumerate(valores):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])
print(f'Número digitados: {valores}')
print(f'A lista pares é: {pares}')
print(f'A lista ímpares é: {impares}')

# Gustavo Guanabara
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')

