from math import radians
import os
import random
os.system("cls")


soma = 0

def sorteio():
    global numeros
    numeros = []

    for i in range (5):
        valores = random.randint(0,100)
        numeros.append(valores)
    return numeros

def soma_par(numeros):
    soma = 0
    for i in numeros:
        if i%2 == 0:
        
            soma = soma + i

    return soma

result = sorteio()
print(result)
print(soma_par(result))

