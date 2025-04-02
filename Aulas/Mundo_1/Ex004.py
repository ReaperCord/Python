#Analisador de palavras

#inicio/cabeçalho
print("Olá, seja bem-vindo ao analisador de palavras")

#Entrada de dados
palavras = input("Digite uma palavra: ")

#Processamento
print("Esta palavra é um: {}".format(type(palavras)))
print("Palavra  é alfanumérica? {}".format(palavras.isalnum()))
print("Palavra é alfabética? {}".format(palavras.isalpha()))
print("Palavra esta em maiúsculo? {}".format(palavras.isupper()))
print("Palavra esta em minúsculo? {}".format(palavras.islower()))
print("Palavra esta capitalizada? {}".format(palavras.istitle()))
print("Palavra tem espaços? {}".format(palavras.isspace()))
print("Palavra tem números? {}".format(palavras.isnumeric()))




