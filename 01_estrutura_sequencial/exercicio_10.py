# Exercício 10
# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# Formula
# F = (C * 9/5) + 32

temperatura = float(input("Informe a temperatura em graus Celsius: "))

fahrenheit = (temperatura * 9/5) + 32

print(f"A temperatura equivalente a {temperatura} C° é {fahrenheit} F°.")
