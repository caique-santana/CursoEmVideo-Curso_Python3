# Exercicío 112
# Caique Santana


def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() or ',' in n or '.' in n:
            valor = float(n.replace(',', '.'))
            ok = True
        else:
            print(f'\033[1;31mERRO: "{n.strip()}" é um preço inválido!\033[m')
        if ok:
            break
    return valor

# Gustavo Guanabara


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
