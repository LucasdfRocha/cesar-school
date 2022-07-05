import os
os.system("cls")

def horasSeg(hora):
    segundos = hora*3600
    return segundos

def horasMin(hora):
    minutos = hora*60
    return minutos


print("--------- CONVERSOR DE HORA PARA MINUTO/SEGUNDO---------")
try:
    resp = int(input("Digite [0] para tranformar de hora para minuto OU Digite [1] para transformar de hora para segundos. "))
    horas = float(input("Digite a quantidade em horas que voce deseja converter: "))

    os.system("cls")
    if resp == 0:
        print(f"{horas} horas em minutos é o equivalente a {horasMin(horas)} minutos ")
    elif resp == 1:
        print(f"{horas} horas em segundos é o equivalente a {horasSeg(horas)} segundos")

except ValueError:
    os.system("cls")
    print("Insira apenas numeros!!!")
