nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, sua média é {:.2f}.'.format(nota1, nota2, media))

if media >= 7.0:
    print('O aluno foi aprovado')
elif media>= 5 and media < 7:
    print('O aluno está em recuperação')
else:
    print('O aluno foi reprovado')
