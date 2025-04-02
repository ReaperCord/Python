#Escreva um programa que receba um valor em metros e exiba os valores correspondentes em cm e mm

m = float(input("Digite quantos metros você deseja converter: "))
cm = m * 100
mm = m * 1000

print("O valor em mentos inserido foi de: {}m\n"
      "O valor em centimetros inserido foi de: {}cm\n"
      "O valor em milimetros inserido foi de: {}mm\n"
      .format(m, cm, mm))
