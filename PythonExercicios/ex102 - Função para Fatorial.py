"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial."""
# Caique Santana


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    fat = 1
    for c in range(1, num + 1):
        fat *= c
    print('-' * 30)
    if show:
        for c in range(0, num):
            print(f'{num - c} x ' if c < num - 1 else f'{num - c} = ', end='')
    return fat


numero = int(input('Digite um número para ver seu fatorial: '))
while True:
    mostrar = str(input('Quer mostrar o processo ? [S/N] '))
    if mostrar in 'SsNn':
        break
if mostrar in 'Nn' or len(mostrar) == 0:
    mostrar = False
elif mostrar in 'Ss':
    mostrar = True
print(fatorial(numero, mostrar))
help(fatorial)

# Gustavo Guanabara


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
