nome_motorista = input('Digite seu nome: ')
idade_motorista = int(input('Qual a sua idade? '))
habilitacao = input('Você possui uma habilitacão? (sim/não) ').lower()

#Cuidado para não colocar == numa variável criada dentro de um If para gerar um boolena
if habilitacao == 'sim':
    carteira_motorista = True
else:
    carteira_motorista = False

# A linha a baxio já é uma expressão booleana
maior_de_idade = idade_motorista >= 18

print('\n--- Informações do Usuário ---')
print('Nome: {} (Tipo: {})'.format(nome_motorista, type(nome_motorista)))
print('Idade: {} (Tipo: {})'.format(idade_motorista, type(idade_motorista)))
print('Possui carteria de motorista: {} (Tipo: {})'.format(carteira_motorista, type(carteira_motorista)))
print('É maior de idade: {} Tipo: {}'.format(maior_de_idade, type(maior_de_idade)))




