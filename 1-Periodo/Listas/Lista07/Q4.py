import os
os.system("cls")

Arquivo = open("notas.txt","r")

for palavras in Arquivo:
    words = palavras.split()
    if len(words) > 7:
        print(words[0])

#ana, nao entendi pra que usar o fileNotFoundError se voce nao pede pro usuario digitar o arquivo.