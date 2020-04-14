""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""
n = 0
cont = 1
while True:
    n = int(input('Digite um número para ver a tabuada: '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n * cont}')
        cont += 1
    print('='*15)
    cont = 1
print('PROGRAMA ENCERRADO!')