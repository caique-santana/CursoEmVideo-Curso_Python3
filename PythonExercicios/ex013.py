# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário do funcionário? '))
print('Com 15% de aumento o salário vai ficar: R${:.2f}'.format(salario + (salario * 0.15)))

# Gustavo Guanabara
salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))