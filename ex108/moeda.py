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
