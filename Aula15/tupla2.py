import os
os.system("cls")

tupla = ()

alunos = int(input("Quantos alunos voce quer avaliar? "))

for i in range (alunos):
    nome =(input("Qual seu nome? "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
media = (nota1 + nota2 + nota3)/3

