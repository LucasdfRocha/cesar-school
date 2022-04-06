import os
os.system("cls")

a = int(input(" Por favor insira um valor para  a: "))
b = int(input("Agora um para b: "))

equacao = 4*a + 3 == b

if equacao == True:
    print("a equacao é satisfeita pelos valores:",equacao)
else:
    print("A equacao é satisfeita pelos valores:", equacao)