"""Calculator program in Python by euvincenzo"""
import math
a = 99999999999999
while a != 0:
    valor1 = float(input("Insira um valor: "))
    valor2 = float(input("Insira outro valor: "))
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    operação = int(input("O que deseja fazer com esses calores? "))
    if operação == 1:
        soma = valor1 + valor2
        print(soma)
    if operação == 2:
        sub = valor1 - valor2
        print(sub)
    if operação == 3:
        mult1 = valor1 * valor2
        print(mult1)
    if operação == 4:
        div = valor1 / valor2
        print(div)

print("Esse programa foi útil? ")
feedback = int(input("Digite 1 para sim e 2 para não"))
goodbye = input("Digite 'sair' para sair do programa. ")


