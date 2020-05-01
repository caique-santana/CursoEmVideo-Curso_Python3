""" Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais """
# Meu
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O \033[1;34mPRIMEIRO\033[m valor é o maior')
elif num2 > num1:
    print('O \033[1;34mSEGUNDO\033[m valor é o maior')
else:
    print('Os dois valores são \033[1;36mIGUAIS\033[m.')

# Gustavo Guanabara
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
