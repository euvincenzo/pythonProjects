"""
Sorteador. Por Vincenzo

"""
import random
print("SORTEADOR DE NÚMERO")
lista = []
while lista != 0:
    num = int(input("Insira um número: "))
    lista.append(num)
    if num == 0:
        break
lista.remove(0)
print(random.choice(lista))