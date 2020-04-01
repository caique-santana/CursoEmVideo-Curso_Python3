# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatuda em graus celsius: '))
fahrenheit = (celsius * (9 / 5)) + 32
print('O valor de {}ºC, será {}ºF'.format(celsius, fahrenheit))

# Gustavo Guanabara
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
