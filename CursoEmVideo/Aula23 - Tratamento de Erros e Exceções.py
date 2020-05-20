try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# Except retorna caso de erro
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:  # Retorno caso não de erro
    print(f'O resultado é {r:.1f}')
finally:  # Retorno se der ou não erro
    print('Volte sempre! Muito obrigado!')
