import os
os.system("cls")

n = int(input("Por favor insira um numero inteiro: "))
soma = 0
for i in range(1,n,1):
    if n%i==0:
        soma = soma + i

if soma == n:
    print("O numero {} é perfeito".format(n))
else:
    print("O numero {} não é perfeito ".format(n))
