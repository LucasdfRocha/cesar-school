import math
import os
os.system('cls ')

a = float(input("Digite o valor de a: "))

if a!= 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Nao tem raiz real")
    else:
        x = float(-b + math.sqrt(delta))/(2*a)
        x2 = float(-b - math.sqrt(delta))/(2*a)
        print("%.2f" % x)
        print("%.2f" % x2)
