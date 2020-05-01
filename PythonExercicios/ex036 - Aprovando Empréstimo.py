""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. """
#Meu
casa = float(input('Qual o valor da casa ? R$'))
sal = float(input('Qual o seu salário ? R$'))
ano = int(input('Em quantos anos pretende fazer o pagamento ? '))
prestacao = casa / (12*ano)
if prestacao > sal * 0.3:
    print('\033[1;31mEmpréstimo Negado\033[m')
else:
    print('\033[1;32mEmpréstimo Condedido\033[m!\nO valor da prestação será de R${:.2f} por mês'.format(prestacao))

# Gustavo Guanabara
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')