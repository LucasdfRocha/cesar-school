import os
os.system("cls")

soma = 0
soma_coluna = 0
matriz = [[],[],[]]

for i in range (3):
    for j in range (3):
        matriz[i].append(int(input(f"Digite um valor para a posição [{i} {j}]: ")))

for i in range (3):
    for j in range (3):
        print(f"[{matriz[i][j]:^4}]", end = "")
# letra a)
        if matriz[i][j]%2 != 0:
            soma += matriz[i][j]
    print()

print(f"a soma dos numeros impares dessa matriz é igual a {soma}")
#letra b)
for i in range (3):
    soma_coluna += matriz [i][0]

print(f"A soma dos valores da 1 coluna é {soma_coluna}")
# letra c)
for j in range (3):
    menor = min(matriz[2])

    print(f"O menor valor da ultima linha é {menor}")
    break