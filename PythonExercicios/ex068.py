""" Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
cont = soma = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = computador + jogador
    if escolha == 'P' and soma % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Um total de {soma} ',
              end='DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
        break
    elif escolha == 'I' and soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Um total de {soma} ',
              end='DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
        break
    cont += 1
    print(f'Você jogou {jogador} e o computador {computador}. Um total de {soma} ', end='DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('\nVocê Venceu!\nVamos jogar novamente...')
print('\nVocê Perdeu!')
print('=*='*20)
print(f'GAME OVER! Você venceu {cont} vezes.')

