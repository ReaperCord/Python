#Faça um algoritimo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

print("Vamos calcular o preço do produto com desconto!")

prod = float(input("Digite o preço do produto: R$ "))
desconto = prod * 0.05
precoNovo = prod - desconto

print("O preço novo do produto com 5% de desconto é: R$ {:.2f}".format(precoNovo))
