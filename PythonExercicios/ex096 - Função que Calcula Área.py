"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""


def área(larg, alt):
    area = larg * alt
    print(f'A área de um terreno {larg:.1f}x{alt:.1f} é de {area}m².')


print('Controle de Terrenos')
print('-' * 15)
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
