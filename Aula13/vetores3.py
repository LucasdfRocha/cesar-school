lista = [3.5,6.7,1.0,4.9]

lista.insert(1,2.3)
print(lista)

lista.pop()
print(lista)

lista[2] = 9.2
print(lista)

lista.sort()
print(lista)

print(len(lista))

for c,v in enumerate(lista):
    print(f"na posição {c} encontrei o valor {v}")
