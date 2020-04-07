"""Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
# Meu
maior = 0
menor = 1000
for c in range(1, 6):
    peso = float(input('Digite o seu peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    elif maior > peso < menor:
        menor = peso
print('Maior peso: {}Kg\nMenor peso: {}Kg'.format(maior, menor))

# Gustavo Guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
