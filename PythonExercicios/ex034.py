'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Qual o seu salário ? '))
if sal <= 1250:
    print('Você terá um aumento de \033[34m15%\033[m e seu novo salário será \033[4;33mR${:.2f}\033[m!'.format(sal + (sal * 0.15)))
else:
    print('Você terá um aumento de \033[34m10%\033[m e seu novo salário será \033[4;33mR${:.2f}\033[m!'.format(sal + (sal * 0.1)))

# Gustavo Guanabara
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))