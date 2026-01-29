# Exercício 16
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

metros = float(input("Tamanho da área em m²: "))

cobertura_por_litro = 3                             # metros quadrados
lata = 18                                           # litros
valor_lata = 80.00                                  # valor lata de tinta
cobertura_por_lata = lata * cobertura_por_litro     # 54m²

quantidade_latas = math.ceil(metros / cobertura_por_lata)
valor_total = quantidade_latas * valor_lata

print(f"Quantidade de latas: {quantidade_latas}")
print(f"Valor total: {valor_total:.2f}")
