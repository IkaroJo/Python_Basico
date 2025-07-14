from time import sleep

#Contagem regressiva de 10 a 0
for cont in range(10, 0, -1): #O step -1 significa que é de trás pra frente
    print(cont)
    sleep(0.5)
print('Kabooom!!')