import os
os.system("cls")

r1 = float(input("Forneça o valor da primeira reta : "))
r2 = float(input("Forneça o valor da segunda reta: "))
r3 = float(input("Agora, forneça o valor da ultima reta: "))

if r1 > 0 and r2 > 0 and r3 > 0:
    if (r2 + r3) > r1 and (r1 + r3) > r2 and (r2 + r1) > r3 :
        print("As 3 retas formam um triangulo")
    else:
        print("as 3 retas nao dão um triangulo")
else:
    print("Forneça numeros positivos!!!")