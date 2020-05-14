"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')"""
# Caique Santana


def leiaInt(num):
    global n
    while True:
        if not n.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            n = input('Digite um número: ')
        else:
            break
    return n


n = input('Digite um número: ')
leiaInt(n)
print(f'Voce acabou de digitar o número {n}')

# Gustavo Guanabara


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
