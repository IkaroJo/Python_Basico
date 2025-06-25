'''
Execício sobre: If, elif, else, operadores (>=, <) e and
'''


print('As notas são representadas de 0 a 100. Dependendo do valor, pode ser do A ao F')
nota_aluno = int(input('Por favor, digite o valor da sua nota: '))

if nota_aluno >= 90:
    print('Sua nota é A')
elif nota_aluno >= 80 and nota_aluno < 90:
    print('Sua nota é B')
elif nota_aluno >= 70 and nota_aluno < 80:
    print('Sua nota é C')
elif nota_aluno >= 60 and nota_aluno < 70:
    print('Sua nota é D')
elif nota_aluno < 60:
    print('Sua nota é F')
else: 
    print('Inválido, tente de novo')


