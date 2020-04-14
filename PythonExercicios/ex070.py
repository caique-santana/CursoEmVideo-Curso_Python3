""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""
continuar = 'S'
total = maisdemil = barato = 0
produto = ''
while continuar == 'S':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if barato == 0:
        barato = preco
    if preco < barato:
        produto = nome
        barato = preco
    if preco > 1000:
        maisdemil += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
print('FIM DO PROGRAMA')
print(f'Total gasto na compra foi R${total:.2f}')
print(f'Foram {maisdemil} produtos que custam mais de R$1.000,00')
print(f'O produto mais barato foi {produto} que custou R${barato:.2f}.')