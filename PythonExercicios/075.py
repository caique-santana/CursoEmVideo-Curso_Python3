""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
# Caique Santana
nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')), int(input('Digite o próximo número: ')))
pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
if nums.count(3) == 0:
    vezes3 = 0
else:
    vezes3 = nums.index(3) + 1
print(f'Você digitou os valores {nums}')
print(f'O número 9 apareceu {nums.count(9)} vezes.')
if vezes3 == 0:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {vezes3}ª posição.')
print(f'Os números pares digitados foram: {pares}')

# Gustavo Guanabara
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end='')
