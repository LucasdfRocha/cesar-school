import os
os.system("cls")


num = int(input("Escolha um numero para verificar se é par ou impar: "))

if num > 0:

    if num%2 == 0:
        print("O numero é par!")
    else:
        print("O numero é Impar!")
else:
    print("digite um numero positivo!!!")