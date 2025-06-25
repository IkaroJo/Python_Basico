'''
Este exercício foca em como você pega informações do usuário (input), transforma essas informações para o tipo certo (int()) e usa um operador (* para multiplicação) para fazer um cálculo, e então exibe o resultado (print).

Em resumo, a sequência de passos é:

Entrada (Input): Obter a idade do usuário.
Processamento (Operação): Multiplicar a idade por 365.
Saída (Output): Mostrar o resultado.

'''

print('A partir da sua idade, irei mostrar quantos dias você já viveu.')
idade = float(input('Quantos anos você tem? '))

dias = idade * 365
meses = (idade * 365) / 30

print('Você já viveu {} dias. Ou aproximadamente {:.2f} meses.'.format(dias, meses))
