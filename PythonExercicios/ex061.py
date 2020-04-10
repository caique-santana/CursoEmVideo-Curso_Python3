"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura WHILE. """
# Meu
primeiro = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))
decimo = primeiro + 10 * raz
while primeiro <= decimo:
    print(primeiro, end=' ')
    primeiro += raz

# Gustavo Guanabara
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ► '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
