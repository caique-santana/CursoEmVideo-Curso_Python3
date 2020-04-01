'''Crie um programa que leia o nome completo de uma pessoa e mostre:
=> O nome com todas as letras maiúsculas.
=> O nome com todas minúsculas.
=> *Quantas letras ao todu (sem considerar espaços).
=> Quantas letras tem o primeiro nome.'''
# Meu
nome = input('Digite seu nome completo: ')
separa = nome.split()
print('Nome em maiúsculo: \033[1;30m{}\033[m'.format(nome.upper()))
print('Nome em minúsculo: \033[1;32m{}\033[m'.format(nome.lower()))
print('Total de letras: \033[1;33m{}\033[m'.format(len(nome.strip(''))))
print('Primeiro nome: \033[1;34m{}\033[m total de letras \033[1;36m{}\033[m'.format(separa[0], len(separa[0])))

# Gustavo Guanabara
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} lentras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))