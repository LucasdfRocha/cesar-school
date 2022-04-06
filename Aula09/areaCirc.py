import os
os.system("cls")

raio = float(input("Digite um valor pro raio para calcular a area: "))

pi = 3.14
area = pi*(raio**2)

print(f"A area do círculo com raio de {raio}, sera igual a {round(area,2)}")