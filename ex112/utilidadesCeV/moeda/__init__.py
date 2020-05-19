def aumentar(n, aut, converte=False):
    aumento = n + (n * aut / 100)
    if converte:
        return moeda(aumento)
    else:
        return aumento


def diminuir(n, dim, converter=False):
    dimi = n - (n * dim / 100)
    if converter:
        return moeda(dimi)
    else:
        return dimi


def dobro(n, converter=False):
    dob = n * 2
    if converter:
        return moeda(dob)
    else:
        return dob


def metade(n, converter=False):
    meta = n / 2
    if converter:
        return moeda(meta)
    else:
        return meta


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, aut, dim):
    print('-' * 33)
    print('         RESUMO DO VALOR     ')
    print('-' * 33)
    print('Preço analisado:', f'{moeda(n):^17}')
    print('Dobro do preço: ', f'{dobro(n, True):^17}')
    print('Metade do preço:', f'{metade(n, True):^17}')
    print(f'{aut} de aumento:  ', f'{aumentar(n,aut, True):^17}')
    print(f'{dim} de redução   ', f'{diminuir(n, dim, True):^17}')
    print('-' * 33)
