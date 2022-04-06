import os
os.system('cls')

somaAlt = 0
mediaAlt = 0

qnt = int(input("Quantos jogadores o seu time possui "))

for i in range(0,qnt):
    altura = float(input("Qual é a altura do jogador? "))

    somaAlt = somaAlt + altura
    mediaAlt = somaAlt/qnt

if mediaAlt > 1.8:
    print("\nTime com jogadores altos!")

else:
    print("\nTime com jogadores de estatura mediana.")
