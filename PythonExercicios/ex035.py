'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''
l1 = float(input('Escreva o valor do 1ª lado: '))
l2 = float(input('Escreva o valor do 2ª lado: '))
l3 = float(input('Escreva o valor do 3ª lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[4;34mÉ possível\033[m fazer um TRIANGULO')
else:
    print('\033[4;31mNão é possível\033[m fazer um TRIANGULO')

# Gustavo Guanabara
print('\033[1;33m-=-\033[m' * 20)
print('Analisador de Triângulos')
print('\033[1;33m-=-\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
