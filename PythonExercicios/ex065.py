""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """
# Meu
soma = maior = menor = cont = 0
continuar = 'S'
while continuar != 'N':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    soma += num
    continuar = str(input('Quer continuar ? [S/N] ')).upper()
print('Você digitou {} número e a média é {:.1f}'.format(cont, soma / cont))
print('O maior foi {} e o menor foi {}'.format(maior, menor))

# Gustavo Guanabara
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {:.1f}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))