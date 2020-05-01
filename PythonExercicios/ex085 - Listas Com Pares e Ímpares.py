"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
# Caique Santana
numeros = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}ª número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores ímpares foram: {numeros[1]}')

# Gustavo Guanabara
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')