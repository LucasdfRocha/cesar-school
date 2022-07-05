import os
os.system("cls")

div = 0

num = int(input("Por favor insira um numero inteiro: "))

if num > 1:
    for i in range (1,num+1):
        if num % i == 0 :
            div += 1
if div == 2:
    print("O numero é primo!")
else:
    print("O numero não é primo!")

