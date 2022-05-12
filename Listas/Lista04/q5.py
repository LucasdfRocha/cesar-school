import os
os.system("cls")

cesar = [[],[],[]]
somaSAL = 0
mediaSAL = 0
somaVT = 0

for i in range (3):
    for j in range (1):

        cesar[i].append(float(input(f"Estagiario {i+1} insira seu salario: ")))

for i in range (3):
    for j in range (1):

        cesar[i].append(float(input(f"Estagiario {i+1} insira seu vale-transporte: ")))

for i in range (3):
    for j in range (1):

        cesar[i].append(float(input(f"Estagiario {i+1} insira seu vale-alimentacao: ")))

for i in range (3):
    somaSAL = somaSAL + cesar[i][0]
    mediaSAL = somaSAL/3.0
    somaVT = somaVT + cesar[i][1]

print("\n  S    VT    VA")
for i in range (3):
    for j in range (3):
        print(f"[{cesar[i][j]:^4}]", end = "")
    print()

print(f"\n A media salarial dos estagiarios foi igual a: {mediaSAL}")
print(f"O total gasto com o vale transporte sera igual a: {somaVT} reais")



#desse modo, ele so pergunta pro proximo estagiario se o que respondeu escrever o salario, vale-transporte e vale-alimentacao primeiro.

""""
import os
os.system("cls")

cesar = [[],[],[]]
somaSAL = 0
mediaSAL = 0
somaVT = 0

for i in range (3):
    for j in range (1):

        cesar[i].append(float(input(f"Estagiario {i+1} insira seu salario: ")))
        cesar[i].append(float(input(f"Estagiario {i+1} insira o valor do seu vale-alimentacao: ")))
        cesar[i].append(float(input(f"Estagiario {i+1} insira o valor do seu vale-transporte: ")))

for i in range (3):
    somaSAL = somaSAL + cesar[i][0]
    mediaSAL = somaSAL/3.0
    somaVT = somaVT + cesar[i][1]

print("\n  S    VT    VA")
for i in range (3):
    for j in range (3):
        print(f"[{cesar[i][j]:^4}]", end = "")
    print()

print(f"\n A media salarial dos estagiarios foi igual a: {mediaSAL}")
print(f"O total gasto com o vale transporte sera igual a: {somaVT} reais")
"""