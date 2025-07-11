from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print(''' Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual sua jogada? '))
print('-='* 10)
print('O jogador escolheu: {}'.format(itens[jogador]))

print('O computador escolher {}'.format(itens[pc]))
print('-='*10)

if pc == 0: #Pc joga Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Jogador perdeu')
    else:
        print('Jogada inválida')


elif pc == 1: #Pc joga Papel
    if jogador == 0:
        print('Jogador perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida')

elif pc ==2: #Pc joga Tesoura
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')