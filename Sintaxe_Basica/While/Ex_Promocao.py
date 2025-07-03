#O While são excelentes Loop quando existe uma condição 
# Crie um While onde o valor do protudo diminua de 5 em 5 até chegar ao preço de custo

valor_produto = 100
dia = 0


while valor_produto > 20:
    dia += 1
    print(f'Hoje é o dia {dia}')
    print(f'Hoje o produto custa R$ {valor_produto}')
    valor_produto -= 5 #Ou = valor_produto - 1
