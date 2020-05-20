# Exercicío 110
# Caique Santana


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
    print(f'{dim} de redução:  ', f'{diminuir(n, dim, True):^17}')
    print('-' * 33)

# Gustavo Guanabara


def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinda preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa /100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
