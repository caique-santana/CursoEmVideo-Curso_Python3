""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag)."""
# Meu
num = cont = soma = 0
print('Para sair digite \033[1;33m999\033[m')
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1
print('Foram digitados {} números e a soma total de todos é {}.'.format(cont, soma))

# Gustavo Guanabara
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))