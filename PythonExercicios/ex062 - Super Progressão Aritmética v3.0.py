""" Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos."""
# Meu (Alguma coisa errada)
primeiro = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))
decimo = primeiro + 10 * raz
while primeiro < decimo:
    print(primeiro, end=' ')
    primeiro += raz
    if primeiro == decimo:
        decimo += int(input('\nQuer mostrar mais quantos números: '))

# Gustavo Guanabara
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ► '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizadas com {} termos mostrados.'.format(total))
