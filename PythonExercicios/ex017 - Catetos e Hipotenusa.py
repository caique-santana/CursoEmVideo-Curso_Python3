# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cO = float(input('cateto oposto: '))
cA = float(input('cateto adjacente: '))
print('O Cateto Oposto é {} e o Cateto Adjacente {} portanto a hipotenusa é {:.2f}'.format(cO, cA, hypot(cO, cA)))

# Gustavo Guanabara

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))