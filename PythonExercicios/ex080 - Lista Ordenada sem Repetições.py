"""Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""
# Caique Santana
valores = []
maior = menor = 0
for i, c in enumerate(range(0, 5)):
    num = int(input(f'Digite o {c+1}ª número: '))
    if c == 0:
        valores.append(num)
        print('Valor inserido na última posição')
        maior = menor = num
    else:
        if num > maior:
            valores.append(num)
            print('Valor inserido na última posição')
            maior = num
        elif num < menor:
            valores.insert(0, num)
            print('Valor adicionado na posição 0')
            menor = num
        elif menor < num < maior:
            valores.insert(valores.index(menor) + 1, num)
            print(f'Valor inserido na posição {valores.index(num)}')
print(valores)

# Gustavo Guanabara
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
