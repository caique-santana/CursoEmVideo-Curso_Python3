"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""
# Meu
from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Feliz Ano Novo :fireworks: :fireworks: :fireworks:'))

# Gustavo Guanabara
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BOOM! BOOM! POOW!')
