import os
from random import randint
os.system("cls")

tupla = []

for i in range (5):
    tupla.append(randint(0,100))
tupla = tuple(tupla)
print(tupla)
print(f"O menor valor da tupla é {min(tupla)}")
print(f"O maior valor da tupla é {max(tupla)}")