import os
os.system("cls")

numeros = []
cont = 0

for i in range (3):
    numeros.append(int(input("Escolha um numero: ")))
    if numeros[i] > 5:
        cont +=1      

media = sum(numeros)/len(numeros)
mediap = (numeros[0]*2 + numeros[1]*4 + numeros[2]*6)/12
#a)
print(f"O maior numero {max(numeros)} insirido no vetor em binario: {max(numeros):b}")
#b)
print(f"A lista tem {cont:x} numeros maiores que 5")
#c)
print(f"A media dos 3 numeros é igual a {media:.3f}")
#d)
print(f"O menor numero insirido, em octal: {min(numeros):o}")
#e)
print(f"A media ponderada dos 3 numeros inseridos é igual a: {mediap:.2f}")



