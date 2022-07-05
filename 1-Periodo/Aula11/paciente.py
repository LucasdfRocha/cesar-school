import os 
os.system("cls")

nome = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))
doenca = input("Voce esta com alguma doença contagiosa? Sim ou Nao ")

if idade >= 65:
    print("Atendimento com prioridade! ")
    if doenca == 'Sim':
        print("O paciente sera encaminhado a sala amarela")
    else:
        print("O paciente sera encaminhado a sala branca")
else:
    print("Atendimento sem prioridade!")
    if doenca == 'Sim' :
        print("O paciente sera encaminhado a sala amarela")
    else:
        print("O paciente sera encaminhado a sala branca")