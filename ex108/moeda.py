# Exercício 108
# Caique Santana


def aumentar(n, aut):
    aumento = n + (n * aut / 100)
    return aumento


def diminuir(n, dim):
    dimi = n - (n * dim / 100)
    return dimi


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    meta = n / 2
    return meta


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

# Gustava Guanabara


def aumentar(n, aut):
    aumentado = n + (n * aut / 100)
    return aumentado


def diminuir(n, dim):
    dimi = n - (n * dim / 100)
    return dimi


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    meta = n / 2
    return meta

# Gustavo Guanabara


def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa /100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
