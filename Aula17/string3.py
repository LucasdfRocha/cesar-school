import os 
os.system("cls")

nome = input("Qual seu nome completo? ").lower()

for i in range (len(nome)): 
    if nome[i] == 's' and nome[i+1] == 'i' and nome[i + 2] == 'l' and nome[i + 3] == 'v' and nome[i + 4] == 'a': 
        print("é da familia silva")
        break
    else:
        print("nao é da familia silva")
        break
        
    