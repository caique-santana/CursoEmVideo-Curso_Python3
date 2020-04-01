# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
reais = float(input('Quantos R$ você tem ? '))
print('Você pode comprar {:.2f} dólares.'.format(reais/5.20))

# Gustavo Guanabara
print('')
real = float(input('Quanto dinheir você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))