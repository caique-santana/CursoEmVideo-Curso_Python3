'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''
# Meu
num = float(input('Qual a distância da viagem: '))
if num <= 200:
    print('O valor da passagem é \033[1;33mR${:.2f}\033[m.'.format(num * 0.5))
else:
    print('O valor da passagem é \033[1;33mR${:.2f}\033[m.'.format(num * 0.45))

# Gustavo Guanabara
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem em {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))