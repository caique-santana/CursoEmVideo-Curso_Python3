#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# Meu
cidade = input('Qual o nome da sua cidade: ')
print('O nome da cidade começa com "Santo" ? \033[1;36m{}\033[m.'.format('SANTO' in cidade.upper().split()[0]))

# Gustavo Guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')