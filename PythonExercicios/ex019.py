# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
aluno1 = input('Escreva o nome do 1ª aluno: ')
aluno2 = input('Escreva o nome do 2ª aluno: ')
aluno3 = input('Escreva o nome do 3ª aluno: ')
aluno4 = input('Escreva o nome do 4ª aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi \033[1m\033[4;31m{}\033[m.'.format(random.choice(alunos)))

# Gustavo Guanabara
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))