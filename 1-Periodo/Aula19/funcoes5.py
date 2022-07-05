import os 
os.system("cls")

def soma(num,num2):

    soma = num + num2
    return soma

def subtracao(num,num2):
    subtracao = num - num2
    return subtracao

def mult(num,num2):
    multiplicacao = num*num2
    return multiplicacao

def abertura():
    print("CALCULADORA")
    print()
    print()
    print()
    print("Escolha a operacao:\n")
    print("1 - soma\n2 - subtracao \n3 - multiplicacao \n4 - divisao\n")
    print("-----------------------------------------")

abertura()
resp = int(input("Escolha a funcao desejada: "))

while resp > 0:

    num = float(input("Escolha um numero: "))
    num2 = float(input("Digite o segundo numero: "))
    

    if resp == 1:
        os.system("cls")
        abertura()
        print("Resultado :",soma(num,num2))
        

    if resp == 2:
        os.system("cls")
        abertura()
        print("Resultado: ",subtracao(num,num2))

    if resp == 3:
        os.system("cls")
        abertura()
        print("Resultado: ",mult(num,num2))

    if resp == 4:

    
    
    resp = int(input("Escolha a funcao desejada: "))




