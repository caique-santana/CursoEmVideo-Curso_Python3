# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# Meu
for c in range(1, 51):
    if c % 2 == 0:
        print(c)

# Gustavo Guanabara
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
