import os
os.system("cls")

arquivo = open("Aula20/media.txt","r")
soma = 0
qtd = 0

for i in arquivo:
    i = float(i)
    soma = soma + i
    qtd += 1
media = soma/qtd
arquivo.close()
print(media)

