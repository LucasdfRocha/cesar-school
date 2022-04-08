import os
os.system("cls")

for i in range (1,31):
    quantidadeFilhos = int(input("Quantos filhos voce tem? "))

    calculoBonus = 150 * quantidadeFilhos
    bonus = print("O seu bonus sera igual a {} reais \n".format(calculoBonus))