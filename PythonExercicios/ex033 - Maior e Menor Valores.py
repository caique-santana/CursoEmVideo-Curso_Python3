# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
n1 = float(input('Escreva o 1ª número: '))
n2 = float(input('Escreva o 2ª número: '))
n3 = float(input('Escreva o 3ª número: '))
cores = {'limpar':'\033[m', 'azul':'\033[34m', 'red':'\033[31m'}
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('{}O mair é {}{}\n{}O menor é {}'.format(cores['azul'], n1, cores['limpar'], cores['red'], n3))
    elif n3 > n2:
        print('{}O maior é {}{}\n{}O menor é {}'.format(cores['azul'], n1, cores['limpar'], cores['red'], n2))
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print('{}O maior é {}{}\n{}O menor é {}'.format(cores['azul'], n2, cores['limpar'], cores['red'], n3))
    elif n3 > n1:
        print('{}O maior é {}{}\n{}O menor é {}'.format(cores['azul'], n2, cores['limpar'], cores['red'], n1))
if n3 > n1 and n3 > n2:
    if n1 > n2:
        print('{}O maior é {}{}\n{}O menor é {}'.format(cores['azul'], n3, cores['limpar'], cores['red'], n2))
    elif n2 > n1:
        print('{}O maior é {}{}\n{}O menor é {}'.format(cores['azul'], n3, cores['limpar'], cores['red'], n1))

# Gustava Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor :'))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
