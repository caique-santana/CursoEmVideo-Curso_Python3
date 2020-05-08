"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo?')

Saida:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""


def escreva(txt):
    print('~' * len(txt))
    print(f'{txt}')
    print('~' * len(txt))


escreva('Caique Santana')
escreva('Curso de Python no YouTube')
escreva('FeP')
