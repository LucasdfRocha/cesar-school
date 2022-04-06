import os
os.system("cls")

qnt = int(input("Quantos funcionarios trabalham na empresa? "))

i = 0

while i < qnt:
    salario = float(input("Digite seu salário: "))
    i+=1

    if salario < 3000:
        aumento = "10%"
        salario = 1.1*salario
    elif salario > 3000 and salario < 5000:
        aumento = "20%"
        salario = 1.2*salario
    elif salario >= 5000 and salario < 7000:
        aumento = "30%"
        salario = 1.3*salario
    else:
        aumento = "35%"
        salario = 1.35*salario

    print(f"O salario após o aumento de {aumento}, sera igual a {salario}\n")