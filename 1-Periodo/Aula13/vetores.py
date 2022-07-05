valores = [2,6,-3,89]

#Mudando o valor de determinado indice
valores[1]= 0
print(valores)

#Adiciona um valor no ultimo indice
valores.append(45)
print(valores)

#Adiciona um valor no indice escolhido
valores.insert(3,234)
print(valores)

#Organiza o vetor em ordem crescente
valores.sort()
print(valores)

#Organiza o valor em ordem decrescente
valores.sort(reverse = True)
print(valores)

#Remove o ultimo indice
valores.pop()
print(valores)

#Remove o indice escolhido
valores.pop(1)
print(valores)


valores.remove(234)
print(valores)

print(len(valores))