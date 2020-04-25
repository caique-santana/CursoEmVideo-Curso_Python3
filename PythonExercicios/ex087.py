"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz = [[], [], [],
          [], [], [],
          [], [], []]
somapares = terceira = maior = 0
for c in range(0, 9):
    num = int(input(f'Digite o {c+1}ª número: '))
    matriz[c].append(num)
    if num % 2 == 0:
        somapares += num
    if c == 2 or c == 5 or c == 8:
        terceira += num
    if 2 < c < 6:
        if num > maior:
            maior = num
print('-=' * 15)
for c in matriz:
    print(f'[ {c[0]} ]', end='')
    if c == [3] or c == [6]:
        print()
print()
print('-=' * 15)
print(f'A soma de todos os pares é {somapares}')
print(f'A soma da terceira coluna é {terceira}')
print(f'O maior valor da 2ª linha é {maior}')
