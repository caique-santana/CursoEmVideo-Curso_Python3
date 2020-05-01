"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta."""
# Caique Santana
from random import randint
from time import sleep
completos = []
palpite = []
jogos = int(input('Quantos jogos você quer fazer ? '))
print(f'SORTEANDO {jogos} JOGOS')
print('-=' * 18)
for c in range(0, jogos):
    sleep(1)
    for n in range(0, 6):
        num = randint(1, 60)
        while num in palpite:
            num = randint(1, 60)
        palpite.append(num)
    palpite.sort()
    completos.append(palpite[:])
    palpite.clear()
    print(f'Jogo {c+1}: ', end='')
    print(completos[0])
    completos.clear()

# Gustavo Guanabara
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA        ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
