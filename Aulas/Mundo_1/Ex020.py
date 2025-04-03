#Sifudemetro agora para apresentação de trabalhos

import random

print("Olá, bom-vindo ao sefudômetro para apresentações de seminário!")
alunos = ["Fulano", "Ciclano", "Beltrano", "Lorem Ipsum"]
originais = alunos.copy()

random.shuffle(alunos)


print("Hoje vamos escolher qual será a ordem de apresentação dos projetos.\n"
      "Os alunos {}, serão organizados randomicamente para apresentação desse projeto que eu tenho certeza que nenhum de vocês fez da forma que ele deveria ser feito...\n"
      "A ordem de apresentação será: {}"
      .format(originais, alunos))
