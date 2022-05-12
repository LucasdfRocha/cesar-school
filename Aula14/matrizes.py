import os
os.system("cls")

matriz = [[],[],[]]

for i in range (3):
    for j in range (3):
        matriz[i].append(int(input(f"Digite um valor para a posição [{i} {j}]: ")))

for i in range (3):
    for j in range (3):
        print(f"[{matriz[i][j]:^4}]", end = "")
    print()