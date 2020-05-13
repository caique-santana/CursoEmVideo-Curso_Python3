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
    print(f"{cores['Limpar']}{cores['FVerde']}~" * 27)
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('~' * 27)
    print(f"{cores['Limpar']}")


while True:
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando == 'fim':
        print(f"{cores['FVermelho']}~" * 13)
        print('  ATÉ LOGO!  ')
        print('~' * 13)
        print(f"{cores['Limpar']}")
        break
    ajuda(comando)
