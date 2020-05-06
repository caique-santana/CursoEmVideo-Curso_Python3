"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
# Caique Santana
from datetime import date
atual = date.today().year
dados = {'nome': str(input('Nome: ')), 'idade': atual - int(input('Ano de Nascimento: ')),
         'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - atual)
print('-=' * 30)
for i, k in dados.items():
    print(f'{i} tem o valor {k}')

# Gustavo Guanabara
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')
