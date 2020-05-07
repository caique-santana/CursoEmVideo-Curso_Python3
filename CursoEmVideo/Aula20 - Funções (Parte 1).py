# Primeiro
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


# Programa Principal
soma(b=4, a=5)
soma(7, 2)


# Segundo
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# Terceiro
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


# Quarto
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
