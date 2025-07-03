'''linha = int(input('Digite quantas linhas deseja: '))
coluna = int(input('Digite quantas colunas deseja: '))
simbolo = input('Digite qual simbolo deseja: ')

for l in range(linha): #Loop das linhas 
    for c in range(coluna): #Loop das colnas
        print(simbolo, end='')
    print() #Serve com um Enter para cada loop l


'''

num_linhas = 5

for i in range(1, num_linhas + 1):
    for j in range(i):
        print('Banzai', end='')
    print()