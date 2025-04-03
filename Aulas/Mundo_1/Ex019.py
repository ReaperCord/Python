#Faça um programa que leia o nome de 4 alunos e escolha 1 para limpar o quadro
import random

print("Bem-vindo a sifudomêtro, aonde um aluno será escolhido para limpar o quadro")

alunos = ["Fulano", "Ciclano", "Beltrano", "Lorem Ipsum"]

print("Dentre os alunos: {}".format(alunos))
print("O aluno que se fudeu e vai limpar o quadro é: {}".format(random.choice(alunos)))
