import os
os.system("cls")


file = open("Aula20/dados.txt","r")
texto = file.read()
print(texto)
palavras = len(texto.split())

print(f"O texto tem: {palavras} palavras e {len(texto)} caracteres")


