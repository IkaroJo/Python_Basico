nome_produto = 'Pc'
valor_produto = 2599.99
quant_estoque = 6

valor_estoque = valor_produto * quant_estoque

print('O {} custa R$ {} a unidade, no estoque temos {} unidades do mesmo. Então temos R$ {:.2f} em produtos.'.format(nome_produto, valor_produto, quant_estoque, valor_estoque))

print(type(nome_produto)) 
print(type(valor_produto))
print(type(quant_estoque))