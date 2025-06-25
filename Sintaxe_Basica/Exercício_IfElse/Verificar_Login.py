'''
Use operadores de comparação (== e !=) e operadores lógicos (and).
'''

nome_usuario = input('Qual o seu usuário? ')
senha = int(input('Qual a sua senha? '))

if nome_usuario == 'admin' and senha == 12345:
    print('Login bem sucedido!')
elif nome_usuario == 'admin' and senha != 12345:
    print('Senha incorreta')
elif nome_usuario != 'admin' and senha == 12345:
    print('Usuário invalido')