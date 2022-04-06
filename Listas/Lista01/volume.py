import os
os.system("cls")

pi = 3.14
raio = float(input("\nqual raio da esfera que voce deseja utilizar para calcular o volume? "))
volume = (4/3)*(pi*raio**3.0)

print(f"O volume da esfera com raio de  {raio} vai ser igual a {round(volume,2)}")