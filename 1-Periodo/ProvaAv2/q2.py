import os
os.system("cls")

maiorMedia = 0.0
media = 0.0
grupos = {}
mediagrupos = {}

try:
    for i in range (3):
        grupo = input(f"Grupo {i}, digite seu nome: ")
        alturaP1 = float(input("Digite a altura do 1 integrante: "))
        alturaP2 = float(input("Digite a altura do 2 integrante: "))
        alturaP3 = float(input("Digite a altura do 3 integrante: "))
        
        grupos[grupo] = alturaP1,alturaP2,alturaP3

        media = round((alturaP1 + alturaP2 + alturaP3)/3.0)
        

        mediagrupos[grupo] = media

        if maiorMedia < media:
            maiorMedia = media
            nome = grupo

    print(f"Os grupos sao {grupos}")
    print(f"as medias das altura sao: {mediagrupos}")
    print(f"e a maior media foi a do grupo {nome} com a media de {maiorMedia}") 
    
except ValueError:
    os.system("cls")
    print("Insira Apenas Numeros!!! ")