"""Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores."""
# Caique Santana
cores = {'Limpar': '\033[m',
         'FAzul': '\033[1;30;46m',
         'FBranco': '\033[7;30m',
         'FVerde': '\033[1;30;42m',
         'FVermelho': '\033[1;30;41m'}


def ajuda(txt):
    tam = len(txt) + 36
    print(f"{cores['FAzul']}~" * tam)
    print(f"  Acessando o manual do comando '{txt}'  ")
    print('~' * tam)
    print(f"{cores['Limpar']}{cores['FBranco']}")
    help(txt)


while True:
    print(f"{cores['Limpar']}{cores['FVerde']}~" * 27)
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('~' * 27)
    comando = str(input(f"{cores['Limpar']}Função ou Biblioteca > ")).lower()
    if comando == 'fim':
        print(f"{cores['FVermelho']}~" * 13)
        print('  ATÉ LOGO!  ')
        print('~' * 13)
        print(f"{cores['Limpar']}")
        break
    ajuda(comando)

# Gustavo Guanabara
from time import sleep
c = ('\033[m',          # 0 - Sem Cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
