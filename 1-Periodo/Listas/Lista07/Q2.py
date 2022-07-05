import os
os.system("cls")

vetor = []
maior = 0
menor = 0
igual = 0
try:
    for i in range (10):
        vetor.append(float(input("Digite um numero: ")))

    for j in range (len(vetor)):
        if j != 0:
            if vetor[j] > vetor[0]:
                maior = maior + 1
            elif vetor[j] < vetor[0]:
                menor = menor + 1
            else:
                igual = igual + 1
    print(f"{maior} maiores que o primeiro vetor")
    print(f"{igual} iguais ao primeiro vetor")
    print(f"{menor} menores que o primeiro vetor")

except ValueError:
    print("Digite Apenas Numeros!")
