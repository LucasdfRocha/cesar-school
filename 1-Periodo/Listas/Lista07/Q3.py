import os
os.system("cls")
soma = 0
num = 0

programa = input("Voce deseja usar no menu? [S] ou [N]: ").upper()

try:
    while programa == "S":

        print("\nEscolha uma opção: ")
        print("0. Ler o arquivo")
        print("1. Escrever um valor nele")
        print("2. Mostrar a soma dos valores")
        print("3. Sair")
        print("---------------------------")
        resp = int(input())

        if resp == 0:
            Arquivo = open("Numeros.txt","r")
            numeros = (Arquivo.read()).split()
            print(numeros)
            Arquivo.close()
            
        elif resp == 1:
            Arquivo = open("Numeros.txt","a")
            numero = float(input("Digite um numero: "))
            Arquivo.close()
            Arquivo = open("Numeros.txt","r")
            for num in Arquivo:
                num = float(num)
            if numero > num:
                numero = str(numero)
                Arquivo = open("Numeros.txt","a")
                Arquivo.write(numero+"\n")
                Arquivo.close()
            else:
                print("O numero Selecionado é menor do que aqueles ja contidos no arquivo!")


        elif resp == 2:
            Arquivo = open("Numeros.txt","r")
            for num in Arquivo:
                num = float(num)
                soma += num
            Arquivo.close()
            print(f"A soma deu {soma}")
            
        elif resp == 3:
            programa = "N"

except FileNotFoundError:
    os.system("cls")
    print("Arquivo não existe, Digite os numeros antes de tentar ler o arquivo!")
    print("Você saiu do aplicativo")


