#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Meu
nome = input('Escreva seu nome completo: ')
print('Tem "Silva" no seu nome ? \033[1;33m{}\033[m'.format('SILVA' in nome.upper()))

# Gustavo Guanabara
nome = str(input('Qual é seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))