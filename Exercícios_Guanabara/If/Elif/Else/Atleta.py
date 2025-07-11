from datetime import date


ano_atual = date.today().year 
ano_atleta = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_atleta
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 25:
    print('Categoria Sênior')
elif idade > 26:
    print('Categoria Master')