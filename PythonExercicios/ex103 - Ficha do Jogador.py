"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""
# Caique Santana


def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: '))
gol = input('Número de Gols: ')
if len(jogador) == 0:
    if len(gol) > 0:
        ficha(gols=gol)
    else:
        ficha()
elif len(gol) == 0:
    ficha(jogador)
else:
    ficha(jogador, gol)

