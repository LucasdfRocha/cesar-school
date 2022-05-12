import os
os.system("cls")

vetor = []
contMai = 0
contMen = 0
contIg = 0

for i in range (10):
    vetor.append(int(input("Por favor insira um valor: ")))

    if vetor[i] > vetor[0]:
        contMai = contMai + 1
    elif vetor[i] < vetor[0]:
        contMen = contMen + 1
    else:
        contIg = contIg + 1

print(f"{contMai} numeros maiores que o primeiro elemento do vetor")
print(f"{contMen} numeros menores que o primeiro elemento do vetor")
print(f"{contIg-1} numeros iguais ao primeiro elemento do vetor")
