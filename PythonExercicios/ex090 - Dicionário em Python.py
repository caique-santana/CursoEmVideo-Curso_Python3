"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
Média 7 ou mais aprovado"""
# Caique Santana
resultado = {}
resultado['Nome'] = str(input('Nome: '))
resultado['Média'] = float(input(f'Média de {resultado["Nome"]}: '))
if resultado['Média'] >= 7:
    resultado['Situação'] = 'APROVADO'
elif resultado['Média'] > 5:
    resultado['Situação'] = 'RECUPERAÇÃO'
else:
    resultado['Situação'] = 'REPROVADO'
print('-=' * 20)
for k, v in resultado.items():
    print(f'    - {k} é igual a {v}')
# Gustavo Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')