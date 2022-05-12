import os 
os.system("cls")

A = []
B = []
C = []
somaPar = 0
somaImp = 0
contImp = 0

for i in range (5):
    A.append(int(input("Digite um numero inteiro positivo Para A: ")))
for i in range (5):
    B.append(int(input("Digite um numero inteiro positivo Para B: ")))
    
C = A + B

for i in range (10):
    if C[i]% 2 == 0:
        somaPar = somaPar + C[i]
    else:
        contImp +=1
        somaImp = somaImp + C[i]

media = somaImp/contImp

print(f"\nVetor A: {A}")
print(f"Vetor B: {B}")
print(f"Vetor C: {C}")
print(f"A soma dos numeros pares do vetor C: {somaPar}")
print(f"A media dos numeros impares do vetor C: {media}")
print(f"O menor valor do vetor C: {min(C)}")
