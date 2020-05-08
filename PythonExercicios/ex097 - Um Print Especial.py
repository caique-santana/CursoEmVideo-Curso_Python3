"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo?')

Saida:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""
# Caique Santana


def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


escreva('Caique Santana')
escreva('Curso de Python no YouTube')
escreva('FeP')  # Função em Python

# Gustavo Guanabara


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabra')
escreva('Curso de Python no YouTube')
escreva('CeV')
