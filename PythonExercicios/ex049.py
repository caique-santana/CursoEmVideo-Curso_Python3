"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""
# Meu
num = int(input('Digite um número para ver a sua tabuada: '))
mult = 1
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, mult, num * mult))
    mult += 1

# Gustava Guanabara
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
