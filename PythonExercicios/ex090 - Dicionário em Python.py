"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
Média 7 ou mais aprovado"""
resultado = {}
resultado['Nome'] = str(input('Nome: '))
resultado['Média'] = float(input(f'Média de {resultado["Nome"]}: '))
if resultado['Média'] >= 7:
    resultado['Situação'] = 'APROVADO'
else:
    resultado['Situação'] = 'REPROVADO'
for k, v in resultado.items():
    print(f'{k} é igual a {v}')
