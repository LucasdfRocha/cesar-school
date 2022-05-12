import os
os.system("cls")

numeros_nycoly = {'a': 100,'b':200,'c':300}
numeros_theo = {'a': 300,'b':200,'d':400,'c':500,'e':250}

numeros_nycoly.update(numeros_theo)

del numeros_nycoly['d']
del numeros_nycoly['e']

print(numeros_nycoly)