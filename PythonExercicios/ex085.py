"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
numeros = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n+1}ª número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores ímpares foram: {numeros[1]}')

