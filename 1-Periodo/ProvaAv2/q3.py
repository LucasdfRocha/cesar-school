import os
os.system("cls")

def notas(n):

    Arquivo2 = open("notas.txt","r")
    nota = Arquivo2.readlines()
    for notas in nota:
        if notas[0] == n:
            return notas
            

resp = int(input("Voce deseja [0] consultar a nota a partir do nome OU [1] a partir do numero? "))
try:
    if resp == 0:

        aluno = input("Qual nome do Aluno que voce deseja procurar? ").capitalize()
        Arquivo = open("classes.txt","r")
        nome = Arquivo.readlines()
        for nomes in nome:
            if aluno == nomes[2:].strip():
                num = nomes[0]

        print(f"As notas de {aluno} são: {notas(num)[2:]} ") 
        Arquivo.close()

    elif resp == 1:

        numero = input("Qual numero voce deseja pesquisar? ")

        Arquivo = open("classes.txt","r")
        numAluno = Arquivo.readlines()

        for alunos in numAluno:
            if numero == alunos[0]:
                nomeAluno = alunos[2:]

        print(f"As notas de {nomeAluno} são: {notas(numero)[2:]}")
except NameError:
    os.system("cls")
    print("Nome do aluno insirido errado ou aluno nao existe")


            
