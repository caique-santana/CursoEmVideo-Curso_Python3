""" Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
# Meu
from random import randint
cont = soma = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = computador + jogador
    print(f'Você jogou {jogador} e o computador {computador}. Um total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P' and soma % 2 != 0:
        break
    elif escolha == 'I' and soma % 2 == 0:
        break
    cont += 1
    print('Você Venceu!\nVamos jogar novamente...')
print('Você Perdeu!')
print('=*='*20)
print(f'GAME OVER! Você venceu {cont} vezes.')

# Gustavo Guanabara
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 ==0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')