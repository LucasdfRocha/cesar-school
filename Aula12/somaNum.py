import os
os.system('cls')

n1 = int(input("Forneca um valor inicial inteiro: "))
n2 = int(input("Forneca um valor final inteiro: "))

soma = 0

for i in range(n1+1,n2+1):
    if(i%2==0):
        soma = soma + i

print(f"A soma dos numeros pares é igual a {soma}")
