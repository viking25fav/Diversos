import random

a = random.randint(0, 10)
b = int(input("Escolha um número de 0 a 10: "))
             
if b == a:
     print("voce acertou!")
else:
     print("voce errou! O número certo é: ")
     print(a)
