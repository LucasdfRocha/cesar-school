import os
os.system("cls")

vascularizacao =int(input("Essa planta apresenta a presença [1] ou a ausencia [2] de vascularização? "))
sementes = int(input("Essa planta apresenta a presença [1] ou a ausencia [2] de sementes? "))
flores = int(input("Essa planta apresenta a presença [1] ou a ausencia [2] de flores? "))

if vascularizacao == 0 and  sementes == 0 and flores == 0:
    print("A planta é uma Bryophyta!")
elif vascularizacao == 1 and sementes == 0 and flores == 0:
    print("A planta é uma Pteridophyta!")
elif vascularizacao == 1 and sementes == 1 and flores == 0:
    print("A planta é uma Gymnospermae")
elif vascularizacao == 1 and sementes == 1 and flores == 1:
    print("A planta é uma Angiospermae!")
else:
    print("Essa planta não se encaixa em nenhum grupo!")