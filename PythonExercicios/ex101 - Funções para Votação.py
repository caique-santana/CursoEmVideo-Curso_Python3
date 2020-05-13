"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
# Caique Santana
from datetime import date
atual = date.today().year


def voto(nasc):
    idade = atual - nasc
    if idade < 16:
        return print(f'Você tem {idade} anos, seu voto é Negado!')
    elif idade <= 17 or idade >= 65:
        return print(f'Você tem {idade} anos, seu voto é Opcional! ')
    else:
        return print(f'Você tem {idade} anos, seu voto é Obrigatório!')


nascimento = int(input('Digite sua data de nascimento: '))
voto(nascimento)
