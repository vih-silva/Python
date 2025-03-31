import math

numero = int(input("Digite um número inteiro: "))

if math.fmod(numero, 2) != 0:
    print("É impar")
else:
    print("É par")
    
