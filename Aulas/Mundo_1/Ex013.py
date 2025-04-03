#Faça um algoritimo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

print("Vamos calcular o novo salário do funcionário com aumento!")

salario = float(input("Digite o salário do funcionário: R$ "))
aumento = salario * 0.15
novoSalario = salario + aumento
print("O novo salário do funcionário com 15% de aumento é de: R$ {:.2f}".format(novoSalario))
