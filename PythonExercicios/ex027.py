'''Faça um programa que leia o nome completo de uma pessoa, monstrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeira = Ana
última = Souza'''
# Meu
nome = input('Escreva seu nome completo: ')
apart = nome.split()
print('Primeiro nome: \033[1;30m{}\033[m.\nÚltima nome: \033[1;30m{}\033[m'.format(apart[0], apart[len(apart)-1]))

# Gustavo Guanabara
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))