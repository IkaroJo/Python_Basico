print('==================Loja======================')

compra = float(input('Preço da compra: R$ '))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão  
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')

opcao = int(input('Qual é a forma de pagamento? '))

if opcao == 1:
    total = compra - (compra * 10 / 100)
elif opcao == 2:
    total = compra - (compra * 5 / 100)
elif opcao == 3:
    total  = compra
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = compra + (compra * 20 / 100)
    quant_parcela = int(input('Serão quantas parcelas? '))
    valor_parcela = total / quant_parcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(quant_parcela, valor_parcela))


print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compra, total))