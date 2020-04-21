""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 45)
print('{:^45}'.format('LISTAGEM DE PREÇOS'))
print('-' * 45)
print('{:.<40}R${:.2f}'.format(produtos[0], produtos[1]))
print('{:.<40}R${:.2f}'.format(produtos[2], produtos[3]))
print('{:.<40}R${:.2f}'.format(produtos[4], produtos[5]))
print('{:.<40}R${:.2f}'.format(produtos[6], produtos[7]))
print('{:.<40}R${:.2f}'.format(produtos[8], produtos[9]))
print('{:.<40}R${:.2f}'.format(produtos[10], produtos[11]))
print('{:.<40}R${:.2f}'.format(produtos[12], produtos[13]))
print('{:.<40}R${:.2f}'.format(produtos[14], produtos[15]))
print('{:.<40}R${:.2f}'.format(produtos[16], produtos[17]))
print('-' * 45)
