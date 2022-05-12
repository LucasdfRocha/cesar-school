import os
os.system("cls")

def contador(frase2):
    x = len(frase2.split())
    return x 
    
frase = input("DIgite sua frase: ")

print(contador(frase))