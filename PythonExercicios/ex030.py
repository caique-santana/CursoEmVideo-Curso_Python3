# Crie um programa que leia um número inteiro e mostre na tela se ela o PAR ou IMPAR
# Meu
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é \033[7;30m\033[1mPAR\033[m.'.format(num))
else:
    print('O número {} é \033[7;30m\033[1mIMPAR\033[m.'.format(num))

# Gustavo Guanabara
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
