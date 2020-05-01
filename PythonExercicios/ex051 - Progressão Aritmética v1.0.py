"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
# Meu
num = int(input('Escreva um número: '))
raz = int(input('Escreva a razão: '))
for c in range(num, raz * 10, raz):  # Errado (num, num + raz * 10, raz)
    print(c, end=' ► ')

# Gustavo Guanabara
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ► ')
print('ACABOU')
