age = int(input("Por favor insira sua idade: "))

if age < 4 or age > 60:
    print("O ticket vai ser gratuito!")
elif age >= 4 and age <= 17:
    print("O ticket vai custar 20 reais")
else:
    print("o ticket vai custar 30 reais")