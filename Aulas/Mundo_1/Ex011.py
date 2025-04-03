#Faça um programa que leia a largura e altura de uma parede e calcule
#a sua e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro pinta uma area de 2m².

print("Vamos calcular a quantidade de tinta necessária para pintar uma parede!")

larg = float(input("Largura da parede: "))
Alt = float(input("Altura da parede: "))

area = larg * Alt
rendimentoTinta = 2
tinta = area / rendimentoTinta

print("A área da sua parede é de {}m²\n"
      "Para pintar essa área, você precisará de {}L de tinta."
      .format(area, tinta))
