import os
os.system("cls")

nome = input("Qual seu nome? ")
altura = float(input("Qual é sua altura? "))
peso = float(input("Agora digite seu peso: "))

IMC = peso/altura**2

print(f"{nome}, o seu IMC é igual a {round(IMC,2)}")