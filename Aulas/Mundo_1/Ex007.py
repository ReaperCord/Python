#Desenvolva um programa que receba 2 notas de um aluno e calcule a sua média.

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

print("As notas do aluno {} foram: \n"
      "Nota 1: {}\n"
      "Nota 2: {}\n"
      "A média do aluno foi de: {}\n"
      .format(nome, nota1, nota2, media))
