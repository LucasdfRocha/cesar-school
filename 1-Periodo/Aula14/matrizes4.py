import os
os.system("cls")

matriz = [[],[],[],[]]
soma = 0

for i in range (4):
    for j in range (5):
        matriz[i].append(int(input(f"Digite a quantidade vendida no trimestre {i + 1} na regiao {j + 1} ")))
        soma += matriz[i][j]

print(f"a soma das quantidades de garrafas vendidas em todas as regiões foi igual a {soma}")

