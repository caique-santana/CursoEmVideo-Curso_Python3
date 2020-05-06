"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""
# Caique Santana
pessoas = []
dados = {}
cont = idade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    cont += 1
    idade += dados['idade']
    resp = str(input('Quer continuar [S/N] ? '))
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar [S/N] ? '))
    if resp in 'Nn':
        break
media = idade / cont
print('-=' * 30)
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

# Gustavo Guanabara
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista de pessoas que estãoa acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
