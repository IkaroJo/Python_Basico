from random import randint
computador = randint(0, 5)
print('Olá, sou seu computador\nAdivinhe o número que escolhi entre 0 e 5')
acertou = False
tentativa = 1

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    if jogador == computador:
        tentativa += 1
        acertou = True
    else:
        if jogador > computador:
            print('Número alto, tente de novo')
        elif jogador < computador:
            print('Número baixo, tente de novo')
        
print('Você acertou em {} tentativas'.format(tentativa))