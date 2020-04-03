""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média emtre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO """
# Meu
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if  media < 5:
    print('\033[1m\033[4;31mREPROVADO\033[m, sua média foi {:.1f}'.format(media))
elif media >= 5 and media <= 6.9:
    print('\033[1m\033[4;33mRECUPERAÇÃO\033[m, sua média foi {:.1f}'.format(media))
else:
    print('\033[1m\033[4;32mAPROVADO\033[m, sua média foi {:.1f}'.format(media))

# Gustavo Guanabara
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif média < 5:
    print('O aluno está REPROVADO')
elif média >= 7:
    print('O aluno está APROVADO')
