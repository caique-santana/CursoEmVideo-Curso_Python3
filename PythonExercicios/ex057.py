"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto."""
# Meu
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
if sexo != 'M' or sexo != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos, informe o seu sexo: ')).upper()
print('Sexo {} registrado.'.format(sexo))

# Gustavo Guanabara
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
