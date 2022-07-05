import os 
os.system("cls")

def media(n1,n2):
    calculo = (n1+n2)/2
    return calculo

def verificador(calculo):
    if calculo > 6:
        print("aprovado")
    elif 4 < calculo < 6:
        print("Verificacao suplementar")
    else:
        print("Reprovado") 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

mediaFinal = media(nota1,nota2)
verificador(mediaFinal)