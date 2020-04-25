"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta."""
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
    print(completos[0])
    completos.clear()

