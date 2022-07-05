import os 
os.system("cls")

i = 0

decisao = input("Voce deseja calcular um bonus no seu salario? [S] ou [N]: ")

while decisao  == 'S':
    salario = int(input("Qual seu salario? "))
    bonus = 1.1*salario

    print(f"O seu salario apos o bonus de 10% sera de {bonus}\n")