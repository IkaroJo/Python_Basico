compra = False
valor = 'Sua comrpa custou R$ 15'


for tentativa in range(3):

    if compra:
        print('Compra realiza com sucesso')
        print(valor)
        break
else:  
     print('Compra negada')
