"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""
# Caique Santana


def área(larg, alt):
    area = larg * alt
    print(f'A área de um terreno {larg:.1f}x{alt:.1f} é de {area}m².')


print('Controle de Terrenos')
print('-' * 25)
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

# Gustavo Guanabara


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


# Programa Principal
print('  Controle e Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
