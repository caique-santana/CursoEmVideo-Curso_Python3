"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""
pessoas = []
dados = {}
cont = idade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    cont += 1
    idade += dados['idade']
    resp = str(input('Quer continuar [S/N] ? '))
    if resp in 'Nn':
        break
media = idade / cont
print(f'Foram cadastradas {cont} pessoas.')
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for i, p in enumerate(pessoas):
    if pessoas[i]['sexo'] == 'F':
        print(pessoas[i]['nome'], end=' ')
print('\nLista das pessoas que estão acima da média:')
print()
for i, p in enumerate(pessoas):
    if pessoas[i]['idade'] > media:
        print(f'Nome = {pessoas[i]["nome"]}; Sexo = {pessoas[i]["sexo"]}; Idade = {pessoas[i]["idade"]}')
print('<< ENCERRADO >>')
