import os 
os.system("cls")

palavra = input(("Escolha a palavra para verificar se é palindromo: "))

inverso = palavra[::-1]

if inverso == palavra:
    print("é palindromo!")

else:
    print("Não é palindromo!")