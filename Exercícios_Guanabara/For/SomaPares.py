soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite um valor: '))
    
    # Somar somente os números pares informados
    if num % 2 ==0: 
        soma += num
        cont += 1
print('O numeros foram {} e a soma é {}'.format(cont, soma))
