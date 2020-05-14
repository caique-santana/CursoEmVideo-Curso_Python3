"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
# Caique Santana
from datetime import date
atual = date.today().year


def voto(nasc):
    idade = atual - nasc
    if idade < 16:
        return print(f'Você tem {idade} anos, não vota!')
    elif idade <= 17 or idade >= 65:
        return print(f'Você tem {idade} anos, seu voto é Opcional! ')
    else:
        return print(f'Você tem {idade} anos, seu voto é Obrigatório!')


nascimento = int(input('Digite sua data de nascimento: '))
voto(nascimento)

# Gustavo Guanabara


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
