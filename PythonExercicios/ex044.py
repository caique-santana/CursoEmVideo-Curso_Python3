""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros """
valor = float(input('Qual o valor do produto ? '))
pag = int(input('Escolha forma de pagamento \n1 - Vista \n2 - Parcelado: '))
if pag == 1:
    print('')
    vista = int(input('1 - Dinheiro\Cheque \n2 - Cartão ? '))
    if vista == 1:
        print('Você terá um desconto de 10%, o valor era R${:.2f} e agora será R${:.2f}.'.format(valor, valor - valor * 0.1))
    else:
        print('Você terá um desconto de 5%, o valor era R${:.2f} e agora será R${:.2f}'.format(valor, valor - valor * 0.05))
else:
    print('')
    parcela = int(input('Vai pagar em quantas vezes ? '))
    valor2 = valor + (valor * 0.2)
    if parcela == 2:
        print('O valor a ser pago é R${:.2f}'.format(valor))
    else:
        print('O valor é R${:.2f} mas com os 20% de juros o preço total vai ser R${:.2f}\nCada parcela será R${:.2f}'.format(valor, valor2, valor2 / parcela))
