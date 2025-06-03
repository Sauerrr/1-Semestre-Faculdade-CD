# Crie um programa que leia dois números do usuário e mostre o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    maior = num1
else:
    maior = num2
print("O maior número é:", maior)

