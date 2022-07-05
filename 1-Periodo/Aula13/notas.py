import os
os.system("cls")

notas = []

for i in range (5):

    notas.append(float(input("Digite sua nota ")))  
      
media = sum(notas)/len(notas) 
print(f"A media é: {media}")

for i in range (len(notas)):  
    if notas[i] > media:
        print(f"A nota {notas[i]} foi maior que a media ")
        