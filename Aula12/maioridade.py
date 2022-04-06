from datetime import date
import os
os.system("cls")

anoAtual = date.today().year
maioridade = 0
menoridade = 0

for i in range(0,5,1):
    anoNasc = int(input("Qual seu ano de nascimento? "))

    if anoAtual - anoNasc >=18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1

print(maioridade, "Atingiram a maioridade e",menoridade,"Atingiram a menoridade")



