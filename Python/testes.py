import random

a = random.randint(0, 1)
b = int(input("Escolha um número de 0 a 1: "))
             
if b == a:
     print("voce acertou!")
else:
     print("voce errou! O número certo é: ")
     print(a)
