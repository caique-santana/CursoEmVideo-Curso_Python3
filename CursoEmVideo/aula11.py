a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Caique'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;33m', nome, '\033[m'))

nome2 = 'Santana'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome2, cores['limpa']))
