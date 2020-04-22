# Primeira Parte
num = [2, 5, 9, 1]
print(f'Mostrando a lista: {num}')
num[2] = 3
print(f'Trocando o 9 pelo 3: {num}')
num.append(7)
print(f'Adicionando o 7 a lista: {num}')
num.sort()
print(f'Ordenando a lista de forma crescente: {num}')
num.sort(reverse=True)
print(f'Ordenando a lista em ordem inversa: {num}')
num.insert(2, 2)
print(f'Inserindo o número 2 no indice 2: {num}')
num.remove(2)  # remove o primeiro elemento que for encontrado
print(f'Removendo o elemento 2: {num}')
if 4 in num:  # Se colocar um elemento que não existe na lista o .remove vai dar erro
    num.remove(4)
else:
    print('Não achei o número 4')
num.pop()
print(f'Apagando o último elemento usando pop(): {num}')
num.pop(2)
print(f'Apagando o elemento no indice 2: {num}')
print(f'Essa lista tem {len(num)} elementos.')

# Segunda Parte
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')
print('')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Terceira Parte
a = [2, 3, 4, 7]
b = a
b[2] = 8
print('Listas Ligadas')
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('')

print('Lista Copiada')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
