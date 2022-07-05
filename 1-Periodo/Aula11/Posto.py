import os
os.system("cls")

combustivel_cliente = int(input("Com qual combustivel voce deseja preencher? [1] gasolina e [2] Álcool:"))
litro = float(input("Quantos litros voce deseja colocar? "))

if combustivel_cliente == 1:
    if litro <= 10:
        desconto = "3%"
        preco = 0.97*(6*litro)
        
    elif litro > 10 and litro <= 20:
        desconto = "5%"
        preco =  0.95 *(6*litro)
    
    else: 
        desconto = "7%"
        preco = 0.93*(6*litro)

else:
    if litro <= 10:
        desconto = "4%"
        preco = 0.96*(5*litro)

    elif litro > 10 and litro <= 20:
        desconto = "6%"
        preco = 0.94*(5*litro)

    else:
        desconto = "8%"
        preco = 0.92*(5*litro)

print(f"O total do valor a pagar com os descontos de {desconto} será de {round(preco,2)} reais")