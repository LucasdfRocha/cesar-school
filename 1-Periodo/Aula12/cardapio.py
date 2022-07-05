import os 
os.system("cls")

valorFinal = 0
somaPedido = 0
valorPedido1 = 15.00
valorPedido2 = 39.90
valorPedido3 = 5.50
valorPedido4 = 2.00

print("Código \t\t\t  Produto \t\t\t\t Preço Unitário")
print("1 \t\t\t  Almoço simples \t\t\t R$ 15,00")
print("2 \t\t\t  Rodízio \t\t\t\t R$ 39,90")
print("3 \t\t\t  Sobremesa \t\t\t\t R$ 5,50 ")
print("4 \t\t\t  Água  \t\t\t\t R$ 2,00")

print()
decisao = input("Você quer fazer um pedido? [S] ou [N] ")

if decisao == "S":

    pedido = int(input("Qual o codigo do produto que voce quer comprar? "))
    quantidade = int(input("Por favor insira a quantidade do produto que você quer comprar: "))
    if pedido == 1:
        somaPedido = somaPedido + (quantidade * valorPedido1)
    elif pedido == 2:
        somaPedido = somaPedido +(quantidade*valorPedido2)
    elif pedido == 3:
        somaPedido = somaPedido +(quantidade*valorPedido3)
    elif pedido == 4:
        somaPedido = somaPedido +(quantidade*valorPedido4)

    continuar = input("Voce deseja escolher mais algum produto? [S] ou [N]: ")
    if continuar == 'S':
        while continuar == 'S':
            pedido = int(input("Qual o codigo do produto que voce quer comprar? "))
            quantidade = int(input("Por favor insira a quantidade do produto que você quer comprar: "))
            if pedido == 1:
                somaPedido = somaPedido + (quantidade * valorPedido1)
            elif pedido == 2:
                somaPedido = somaPedido +(quantidade*valorPedido2)
            elif pedido == 3:
                somaPedido = somaPedido +(quantidade*valorPedido3)
            elif pedido == 4:
                somaPedido = somaPedido +(quantidade*valorPedido4)
            continuar = input("Voce deseja escolher mais algum produto? [S] ou [N]: ")
            if continuar == 'N':
                pagamento = int(input("Qual vai ser a forma de pagamento, crédito [1] ou debito [2]: "))
                if pagamento == 2:
                    valorFinal = somaPedido * 0.9
                elif pagamento == 1:
                    valorFinal = somaPedido
print(f"O valor da sua conta sera igual a: {valorFinal} reais")





'''
somaPedido = 0
decisao = input("Você quer fazer um pedido? [S] ou [N] ")

while decisao == "S":

    pedido = int(input("Qual o codigo do produto que voce quer comprar? "))
    quantidade = int(input("Por favor insira a quantidade do produto que você quer comprar: "))
    if pedido == 1:
        somaPedido = somaPedido + (quantidade * valorPedido1)
    elif pedido == 2:
        somaPedido = somaPedido +(quantidade*valorPedido2)
    elif pedido == 3:
        somaPedido = somaPedido +(quantidade*valorPedido3)
    elif pedido == 4:
        somaPedido = somaPedido +(quantidade*valorPedido4)

    decisao = input("Voce deseja escolher mais algum produto? [S] ou [N]: ")

// Fora do laço: escolher forma de pagamento e dar o desconto
'''