import os 
os.system("cls")

somaId = 0

for i in range(1,6):
    idade = int(input("Digite a idade para o calculo da media: "))
    somaId = somaId + idade

mediaId = somaId/5.0

print(f"A media das idades vai ser igual a {mediaId}")
