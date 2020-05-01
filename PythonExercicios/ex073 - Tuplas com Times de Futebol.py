""" Crie uma tupla preenchida com os 20 primeiros colocados da Tableda do Campeonato Brasileiro de Futebol,
 a ordem de colocação. Depois mostre:
 A) Apenas os 5 primeiros colocados.
 B) Os últimos 4 colocados da tabela.
 C) Uma lista com os times em ordem alfabética.
 D) Em que posição na tabela está o time da Chapecoense."""
# Caique Santana
colocacao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
             'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
             'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('{:^60}'.format('Campeonato Brasileiro 2017'))
print(f'Classificação Geral: \n{colocacao}')
print('*' * 60)
print(f'Os 5 primeiros colocados são: \n{colocacao[0:5]}')
print('*' * 60)
print(f'Os 4 últimos colocados são: \n{colocacao[-4:]}')
print('*' * 60)
print(f'Os times em ordem alfabética fica: \n{sorted(colocacao)}')
print('*' * 60)
print(f'A Chapecoense está na {colocacao.index("Chapecoense")+1}ª posição.')

# Gustavo Guanabara

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
