sexo = str(input('Infom seu sexo: [M/F] ')).upper().strip().strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dado incorreto, informe seu sexo: [M/F]')).strip().upper()[0]
print('Registrado, você é {}'.format(sexo))