# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.
'''from math import sin, cos, tan
ang = float(input('Digito um ângulo qualquer: '))
print('Ângulo: {}.\nSeno: {:.2f}.\nCosseno: {:.2f}.\nTangente: {:.2f}.'.format(ang, sin(ang), cos(ang), tan(ang)))
'''
# Gustavo Guanabara
from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))