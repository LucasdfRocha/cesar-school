import os
os.system("cls")

idadeAluno = int(input("Qual sua idade? "))
salarioProf = float(input("Professor, por favor diga seu salário: "))

if idadeAluno >= 18:
    print("O aluno é maior de idade! ")
else:
    print("O aluno nao é maior de idade! ")
if salarioProf >=  1212:
    print("O professor recebe mais do que um salario minimo")
else:
    print("O professor nao recebe um salario minimo")