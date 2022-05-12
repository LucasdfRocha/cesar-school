import os
os.system("cls")

matriz = [[],[],[]]
soma = 0

for i in range (3):
    for j in range (4):
        matriz[i].append(float(input(f"aluno {i + 1} Digite sua nota {j + 1}: ")))
        soma += matriz[i][j]

media = soma/12
print(f"A media da turma no geral é igual a {media}")