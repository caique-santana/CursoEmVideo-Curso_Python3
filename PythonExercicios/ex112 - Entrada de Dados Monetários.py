"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamdo dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma
validação de dados para aceitar apenas valores que sejam monetários."""
from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

valor = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(valor, 35, 22)
