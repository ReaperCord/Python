import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

#elevando os valores a quadrado
a = math.pow(a, 2)
b = math.pow(b, 2)

#estabelecendo o teorema de pitagoras a² + b² = c²
c = math.sqrt(a + b)

#resolução
print("O valor da hipotenusa é de: {:.2f}".format(c))
