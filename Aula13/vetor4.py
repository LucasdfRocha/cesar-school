import os
os.system("cls")

lista = []
cont = 0

for i in range (10):

    lista.append( int(input("digite um numero: "))) #type: ignore
      
print("\n",lista)
print(f" O menor numero da lista é {min(lista)}")
print(f"O maior numero da lista foi {max(lista)}")

for i in range (10):
    if lista[i]%2 != 0:
        cont += 1
print(f"Nessa listas temos {cont} numeros impares")