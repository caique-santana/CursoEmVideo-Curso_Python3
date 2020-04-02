"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes """
# Meu
print('\033[1;34m-=-\033[m'*20)
print('\033[33mVamos calcular se podemos formar um triângulo e seu tipo\033[m')
print('\033[1;34m-=-\033[m'*20)
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado:'))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado2 == lado3:
        print('Eles formam um triângulo Equilatero')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Eles formam um triângulo Escaleno')
    else:
        print('Eles formam um triângulo Isósceles')

else:
    print('Os lados não formam um triângulo')