#Faça um programa que leia um numero inteiro e mostre seu sucessor e antecessor


n = int(input("Digite um um número: "))
count = n
contup = (count + 1)
contdown = (count - 1)

print("O antecessor de {} é: {}" .format(n, contup))
print("O numero subsequente {} de é: {}" .format(n, contdown))
