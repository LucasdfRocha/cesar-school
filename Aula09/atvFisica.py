import os
os.system("cls")

altura = 1.65
peso = 56

ativFis = input("Voce pratica atividades fisicas? [S] ou [N]")
Litros = int(input("Quantos Litros você bebe por dia? "))

if ativFis == 'S':
    print(f"Você tem {altura} metros de altura,{peso} Kg,faz atividade física e Bebe {Litros} litros de agua por dia")
else:
    print(f"Você tem {altura} metros de altura,{peso} Kg,não faz atividade física e Bebe {Litros} litros de agua por dia")