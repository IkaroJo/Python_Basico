soma = 0 #Acumulador de valores
c = 0 #Contador geralemnte conta + 1

for cont in range(1, 101, 2):
    if cont % 3 == 0:  #Condicional pra saber se o número é divido por 3
        soma += cont 
        c += 1 
print(f'A soma de tudo é: {soma}')
print(f'Numeros contados é: {c}')