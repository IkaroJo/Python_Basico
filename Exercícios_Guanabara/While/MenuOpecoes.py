from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:

    print(''' 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opção = int(input('Qual é a sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 < n2:
            print('O {} é menor que {}'.format(n1, n2))
        elif n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
    elif opção == 4: 
        print('Informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando')
    else:
        print('Opção inválida, tente novamente.')
    print('-='*10)
    sleep(1.5)
print('Fim do programa!')


