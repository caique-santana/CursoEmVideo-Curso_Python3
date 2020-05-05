"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import date
atual = date.today().year
dados = {'nome': str(input('Nome: ')), 'idade': atual - int(input('Ano de Nascimento: ')),
         'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + 35 - (atual - dados['contratação'])
print('-=' * 30)
print(dados)
for i, k in dados.items():
    print(f'{i} tem o valor {k}')
