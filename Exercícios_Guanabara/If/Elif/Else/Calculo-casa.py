valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o eu salário? R$ '))
anos = int(input('Em quantos anos você quer pagar a casa? '))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa do valor de R$ {valor_casa} em {anos} anos.')
print('A prestação será de R$ {:.2f} por mês.'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')