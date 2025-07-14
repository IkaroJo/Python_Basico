num = int(input('Digite um número: '))

for c in range(1, num +1):
    if num % c == 0:
        print(c)
    else:
        print('')
        
    print('{} é um número primo '.format(c), end='')