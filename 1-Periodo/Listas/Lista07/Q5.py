import os
os.system("cls")
from random import randint

subtracao = 0
soma = 0
num = []
numImp = []
numPar = []

def sorteia():
    for i in range(10):
        num.append(randint(0, 200))
    return num
    
def operacao(pares,numImp):
    global subtracao
    global soma
    for i in range (len(numPar)):
        subtracao = subtracao - pares[i]
    for j in range (len(numImp)):   
        soma = soma + numImp[j]
    print(f"Subtracao dos valores pares:{subtracao}")
    print(f"Soma dos numeros impares {soma}")

print(sorteia())
for k in range(len(num)):
    if num[k]%2==0:
        numPar.append(num[k])
    else:
        numImp.append(num[k])

operacao(numPar,numImp)

