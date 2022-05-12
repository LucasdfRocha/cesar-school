import os
os.system("cls")

matriz = [[],[],[]]
vetorFinal =[]
soma1 = 0.0
soma2 = 0.0
soma3 = 0.0

for i in range (3):
    for j in range (3):
        matriz[i].append(float(input(f"Escolha um numero para linha {i+1} e coluna {j+1}: ")))

for i in range(3):
    soma1 = soma1 + matriz[i][0]
    soma2 = soma2 + matriz[i][1]
    soma3 = soma3 + matriz[i][2] 
vetorFinal.append(soma1)
vetorFinal.append(soma2)
vetorFinal.append(soma3)
print()
for i in range (3):
    for j in range (3):
        print(f"[{matriz[i][j]:^4}]", end = "")
    print()

print(f"\nVetor Com as somas das colunas respectivamente:{vetorFinal}")