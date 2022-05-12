import os
os.system("cls")

temp = []
temp2 = []

for i in range (10):
    temp.append(int(input("Digite a temperatura em Farenheit: ")))

print (f"vetor com as temperaturas em farenheit {temp}") 
for i in range (10):
    celsius =round((((temp[i]-32)*5)/9),2)
    temp2.append(celsius)
print(f"vetor com as temperaturas em celsius:{temp2}")
    
