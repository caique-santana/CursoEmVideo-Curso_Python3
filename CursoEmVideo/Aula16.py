lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' - Esse comando não vai funcionar

print(len(lanche))
print(sorted(lanche))
print(lanche)
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu Vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))
print(f'o tamanho de "c" é {len(c)}')
print(f'Tem {c.count(5)} números 5')

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)
