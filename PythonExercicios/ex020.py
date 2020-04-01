# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
'''import random
aluno1 = input('Escreva o nome do 1ª aluno: ')
aluno2 = input('Escreva o nome do 2ª aluno: ')
aluno3 = input('Escreva o nome do 3ª aluno: ')
aluno4 = input('Escreva o nome do 4ª aluno: ')
alunos = aluno1, aluno2, aluno3, aluno4
print('A ordem de apresentação será {}'.format(random.choices(alunos)))'''

# Gustavo Guanabara
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)