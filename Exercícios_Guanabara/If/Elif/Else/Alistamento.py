from datetime import date
ano_atual = date.today().year
ano_nasci = int(input('Qual seu ano de nascimento? '))
idade = (ano_atual) - (ano_nasci)
print(f'Quem nasceu em {ano_nasci} tem {idade} em {ano_atual}')

if idade == 18:
    print('Seu alistamento é esse ano')

elif idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print('Ainda faltam {} para seu alistamento'.format(saldo))
    print('Seu alistamento será em {} anos.'.format(ano))

elif idade > 18:
    saldo2 = idade - 18
    ano = ano_atual - saldo2
    print('Deveria ter se alistado a {} anos'.format(saldo2))
    print('Seu alistamento foi em {} '.format(ano))