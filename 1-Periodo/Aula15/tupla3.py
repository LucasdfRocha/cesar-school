import os
os.system("cls")

pagina = int(input("qual pagina voce esta: "))

if 1<=pagina <= 40:
    print("é o primeiro topico")
elif 40<pagina <=80:
    print("É o segundo topico")
elif 80 < pagina <= 120:
    print("É o terceiro topico")
elif 120 < pagina <= 160:
    print("é o quarto topico")
elif 160 < pagina <= 200 :
    print("É o ultimo topico")
