import os
os.system("cls")

nomes = []
sobrenomes = []
idades = []

Arquivo = open("informacoes.txt","a")

qtd = int(input("Quantas pessoas voce deseja cadastrar? "))
Arquivo.write(f"Ha {qtd} pessoas cadastradas\n")

for i in range (qtd):

    nome = (input("Qual seu nome: "))
    nomes.append(nome)
    
    sobrenome = (input("Qual seu sobrenome: "))
    sobrenomes.append(sobrenome)
    
    idade = (input("Qual sua idade: "))
    idades.append(idade)

for j in range (len(nomes)):
    Arquivo.write("Nome: "+ nomes[j] + " "+ sobrenomes[j]+ " "+ "idade:"+ idades[j])
    Arquivo.write("\n")
    
Arquivo.close()

    
