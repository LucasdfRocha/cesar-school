import os
os.system("cls")

consumo = float(input("Digite o seu consumo de energia em kw "))

taxa = 5

if consumo <= 500:
    tarifa = 0.02
    conta = tarifa * consumo + taxa
elif consumo > 500 and consumo < 1000:
    tarifa = 10
    conta = tarifa * consumo + taxa
else:
    tarifa = 35
    conta = tarifa * consumo + taxa

print(f"O valor da sua conta com a tarifa de {tarifa} sera de {conta}")