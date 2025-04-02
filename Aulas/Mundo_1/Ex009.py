#faça um algoritimo que receba um numero inteiro qualquer e mostre na tela a sua tabuada

n = int(input("Digite um número inteiro: "))
tabuada = 0

while tabuada <= 10:
    print("{} x {} = {}".format(n, tabuada, tabuada*n))
    tabuada += 1
