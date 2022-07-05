import os
os.system("cls")

nome = input("Qual seu nome? ").capitalize()
sobrenome = input("Qual seu sobrenome? ").capitalize()
dataAniv = input("Qual o dia do seu aniversario? ")
mesAniv = input("Qual o mes do seu aniversario? ")
AnoNiv = input("Qual o ano do seu aniversario? ")

nomeFinal = (nome,sobrenome)
nomec = " ".join(nomeFinal)

aniversario = dataAniv + "/" + mesAniv + "/" + AnoNiv

print(f"{nomec} seu aniversario é {aniversario}")