""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""
# Meu
total = maisdemil = barato = 0
produto = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if barato == 0:
        produto = nome
        barato = preco
    if preco < barato:
        produto = nome
        barato = preco
    if preco > 1000:
        maisdemil += 1
    total += preco
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total gasto na compra foi R${total:.2f}')
print(f'Foram {maisdemil} produtos que custam mais de R$1.000,00')
print(f'O produto mais barato foi {produto} que custou R${barato:.2f}.')

# Gustavo Guanabara
total = totlmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totlmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totlmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')