'''
Use os operadores de comparação (>=, <, <=) e o operador lógico and.
'''

print('Preciso validar sua idade')
idade_usuario = int(input('Quantos anos você tem? '))

if idade_usuario >= 18:
    print('Pode entrar na balada e votar')
elif idade_usuario == 16 and idade_usuario == 17:
    print('Pode votar, mas não pode entra na balada')
else:
    print('Não pode votar nem entrar na balada')

