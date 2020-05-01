'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
# Meu
vel = float(input('Qual a velocidade do carro em Km ? '))
if vel > 80:
    print('\033[1m\033[4;31mVocê foi multado\033[m, o valor da multa é \033[1;33mR${:.2f}\033[m.'.format((vel - 80) * 7))
print('Tenha um bom dia!')

# Gustavo Guanabara
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança')