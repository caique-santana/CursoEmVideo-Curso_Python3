""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros """
# Meu
valor = float(input('Qual o valor do produto ? '))
pag = int(input('''Escolha forma de pagamento 
[ 1 ] - Vista
[ 2 ] - Parcelado
Opção escolhida: '''))
if pag == 1:
    vista = int(input('''    [ 1 ] - Dinheiro\Cheque 
    [ 2 ] - Cartão 
    Opção escolhida ? '''))
    if vista == 1:
        print('Você terá um desconto de 10%, o valor era R${:.2f} e agora será R${:.2f}.'.format(valor, valor - valor * 0.1))
    elif vista == 2:
        print('Você terá um desconto de 5%, o valor era R${:.2f} e agora será R${:.2f}'.format(valor, valor - valor * 0.05))
    else:
        print('Opção Inválida!')
elif pag == 2:
    parcela = int(input('Vai pagar em quantas vezes ? '))
    valor2 = valor + (valor * 0.2)
    if parcela == 2:
        print('O valor a ser pago é R${:.2f}'.format(valor))
    else:
        print('O valor é R${:.2f} mas com pagamento com mais de 2 parcelas tem 20% de juros e o preço total vai ser R${:.2f}\nCada parcela será R${:.2f}'.format(valor, valor2, valor2 / parcela))
else:
    print('Opção Inválida!')

# Gustavo Guanabara
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
