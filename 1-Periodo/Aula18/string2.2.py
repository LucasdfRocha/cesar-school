import os
os.system("cls")


lista = []
soma = 0

for i in range (10):
    lista.append(int(input("Digite um numero: ")))

for i in range (11):
    soma  += lista.count(i+10)

print(soma)

    
    

