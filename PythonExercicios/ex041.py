"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: Sênior
Acima: MASTER"""
# Meu
from datetime import date
ano = int(input('Em qual ano você nasceu ? '))
idade = date.today().year - ano
if idade <= 9:
    print('Sua idade é {}\nCategoria: Mirim'.format(idade))
elif idade <= 14:
    print('Sua idade é {}\nCategoria: Infantil'.format(idade))
elif idade <= 19:
    print('Sua idade é {}\nCategoria: Junior'.format(idade))
elif idade <= 20:
    print('Sua idade é {}\nCategoria: Sênior'.format(idade))
else:
    print('Sua idade é {}\nCategoria: Master'.format(idade))
