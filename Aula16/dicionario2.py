import os
os.system("cls")

situacao = {"jose":"vivo","manuel":"vivo","andre":"morto"}

relacao = list(situacao.values())
nomes = list(situacao)

for i in range (3):

    if relacao[i] == "vivo": 
        print(f"{nomes[i]} esta {relacao[i]}")
        