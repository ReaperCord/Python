#Crie um programa que verifique quanto alguem tem na carteira e
#veja quantos dolares ele pode comprar, Dolar = 5.23

carteira = float(input('Digite o valor do carteira: '))
dolar = 5.23

podeComprar = carteira/dolar

print("Com R$ {} você pode comprar: USD$ {:.3f} " .format(carteira, podeComprar))
