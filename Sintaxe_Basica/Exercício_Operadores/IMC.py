print ('Iremos nesse momento coletar algumas infomrações sobre você. Por favor, responda corretamento.')

nome = str(input('Qual o seu nome? '))
idade = input('Qual a sua idade? ')
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))

IMC = peso/altura**2 

print('De acordo com seus dados, com {} anos, você tem um IMC de {:.2f}.'.format(idade, IMC))
