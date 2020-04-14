""" Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
nota50 = nota20 = nota10 = nota1 = 0
valor = int(input('Qual o valor a ser sacado: R$'))
while True:
    if valor == 0:
        if nota50 > 0:
            print(f'Total de {nota50} notas de R$50')
        if nota20 > 0:
            print(f'Total de {nota20} notas de R$20')
        if nota10 > 0:
            print(f'Total de {nota10} notas de R$10')
        if nota1 > 0:
            print(f'Total de {nota1} notas de R$1')
        print('-*' * 20)
        break
    if valor % 50 == 0:
        nota50 += 1
        valor -= 50
    elif valor % 20 == 0:
        nota20 += 1
        valor -= 20
    elif valor % 10 == 0:
        nota10 += 1
        valor -= 10
    elif valor % 1 == 0:
        nota1 += 1
        valor -= 1
print('Saque feito com sucesso!\nTenha um bom dia!')