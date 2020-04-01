'''Faça um programa que leia uma frase pelo teclado e mostre:
=> Quantas vezes aparece a letra "A".
=> Em que posição ela aparece a primeira vez.
=> Em que posição ela aparece a última vez.'''
# Meu
frase = str(input('Escreva uma frase: ')).strip()
input('A letra "A" aparece: \033[1;34m{}\033[m\nEla aparece pela primeira vez no posição: \033[1;30m{}\033[m\nEla aparece por último no posição: \033[1;33m{}\033[m'.format(frase.upper().count("A"), frase.upper().find("A")+1, frase.upper().rfind("A")+1))

# Gustavo Guanabara
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
