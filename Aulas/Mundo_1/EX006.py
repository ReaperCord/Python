#Crie um algoritimo que mostre um numero, o seu dobro o seu triplo e sua raiz quadrada

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = n ** 2

print("O número digitado foi: {}\n"
      "O dobro do número digitado é: {}\n"
      "O triplo do número digitado é: {}\n"
      "A raiz quadrada do numero digitado é: {}"
      .format(n, dobro, triplo, raiz))