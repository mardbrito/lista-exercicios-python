# Exercício 09
# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# Formula
# C = 5 * ((F-32) / 9).

temperatura = float(input("Informe a temperatura em graus Fahrenheit: "))

celsius = 5 * ((temperatura - 32) / 9)

print(f"A temperatura equivalente a {temperatura} F° é {celsius} C°.")
