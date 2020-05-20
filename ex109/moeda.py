# Exercício 109
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

# Gustavo Guanabara


def aumentar(preço=0, taxa=0, formato=False):
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
