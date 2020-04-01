# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input('Digite um número: '))
print('Você digitou o número {}.\nSeu sucessor é {}.\nSeu antecessor é {}'.format(numero, numero+1, numero-1))
print('')

# Gustavo Guanabara
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
print('')

# Segunda forma
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))