import math

angulo = float(input("Digite o ângulo em graus: "))
angulo_rad = math.radians(angulo)  # Converte para radianos

senoA = math.sin(angulo_rad)
cosenoA = math.cos(angulo_rad)
tangenteA = math.tan(angulo_rad)

print("O valor do seno é: {}" .format(senoA))
print("O valor do cosseno é: {}" .format(cosenoA))
print("O valor da tangente é: {}" .format(tangenteA))

