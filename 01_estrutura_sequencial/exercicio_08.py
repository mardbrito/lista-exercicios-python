# Exercício 08
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = float(input("Quanto você ganha por hora trabalha? "))
horas = float(input("Quantas horas você trabalhou durante o mês? "))

salario = valor * horas

print(f"Salário do mês: {salario:.2f}")
