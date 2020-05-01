""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""
# Meu
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

# Gustavo Guanabara
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
