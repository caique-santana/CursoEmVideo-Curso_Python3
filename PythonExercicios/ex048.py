"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalor de 1 até 500."""
# Meu
soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print('A soma de todos os valores é igual à {}.'.format(soma))

# Gustava Guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       soma += c
       cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
