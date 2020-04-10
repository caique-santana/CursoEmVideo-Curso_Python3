'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
# Meu
from time import sleep
opcao = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while opcao != 5:
    opcao = int(input(''' [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos Números
 [5] Sair do programa
 Escolha a opção:'''))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'. format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
    print('=*='*15)
    sleep(3)

# Gustavo Guanabara
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto =  n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Programa finalizado! Volte sempre.')
