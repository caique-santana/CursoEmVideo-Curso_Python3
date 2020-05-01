"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA"""
# Meu
print('\033[1;34m-=-\033[m'*15)
print('\033[1;33mVamos descobrir se a frase é um palíndromo\033[m')
print('\033[1;34m-=-\033[m'*15)
frase = str(input('Escreva uma frase: ')).upper().replace(' ', '')
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('\033[1;32mÉ um palíndromo!\033[m')
else:
    print('\033[1;31mNÃO É um palíndromo!\033[m')

# Gustavo Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto [::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
