'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex: Digite um número:1834
unidade:4
dezena:3
centena:8
milhar:1'''
# Meu
num = input('\033[7;30mDigite um número entre 0 e 9999: \033[m')
print('unidade: \033[1;30m{}\033[m\ndezena: \033[1;36m{}\033[m\ncentena: \033[1;35m{}\033[m\nmilhar: \033[1;33m{}\033[m'.format(num[3], num[2], num[1], num[0]))

#Gustavo Guanabara
num = int(input('Informa um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))