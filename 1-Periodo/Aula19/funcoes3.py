import os
os.system("cls")

def ficha(n,g):
    print(f"{n} fez {g} gols")

nome = input("Qual seu nome? ")
gols = int(input("Quantos gols voce fez? "))

ficha(nome,gols)