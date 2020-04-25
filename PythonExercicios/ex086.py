"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
matriz = [[], [], [],
          [], [], [],
          [], [], []]
for c in range(0, 9):
    matriz[c].append(int(input('Digite um número: ')))
print('-=' * 15)
for c in matriz:
    print(f'[ {c[0]} ]', end='')
    if c == [3] or c == [6]:
        print()
