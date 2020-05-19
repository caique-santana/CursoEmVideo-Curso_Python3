"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
from ex107 import moeda

valor = float(input('Digite um preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13)}')
