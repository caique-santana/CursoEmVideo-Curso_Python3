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
    print('O valor da prestação será de R${} por mês'.format(prestacao))