def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() or ',' in n:
            valor = float(n.replace(',', '.'))
            ok = True
        else:
            if n == '':
                n = '""'
            print(f'\033[1;31mERRO: {n} é um preço inválido!\033[m')
        if ok:
            break
    return valor

