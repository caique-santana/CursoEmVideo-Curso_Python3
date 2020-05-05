"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador."""
jogadores = list()
dados = dict()
gols = list()
total = 0
while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou ? '))
    for c in range(0, dados['partidas']):
        num = int(input(f'Quantos gols na partida {c+1} ? '))
        gols.append(num)
        total += num
    dados['gols'] = gols[:]
    dados['total'] = total
    gols.clear()
    total = 0
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
    print('-' * 50)
print('-=' * 30)
print(f'{"cod":<2} {"nome":<10} {"gols":<13} {"total":>10} ')
print('-' * 42)
for k, v in enumerate(jogadores):
    print(f'{k:<2} {v["nome"]:<10} {v["gols"]} {v["total"]:>2}')
while True:
    print('-' * 42)
    opcao = int(input('Mostra dados de qual jogador ? '))
    if opcao == 999:
        break
    elif opcao > len(jogadores):
        print(f'ERRO! Não existe jogador com código {opcao}! Tente novamente.')
    else:
        print('-' * 2, 'LEVANTAMENTO DO JOGADOR', f'{jogadores[opcao]["nome"]}')
        for k, v in enumerate(jogadores[opcao]["gols"]):
            print(f'    No jogo {k+1} fez {v} gols.')
print('<< VOLTE SEMPRE >>')
