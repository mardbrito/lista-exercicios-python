# Exercício 17
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Tamanho da área em m²: "))

cobertura_por_litro = 6                             # m²
lata_litros = 18                                    # litros
galao_litros = 3.6                                  # litros
preco_lata = 80.00                                  # preço da lata de tinta
preco_galao = 25.00                                 # preço do galao

# calculos
litros_necessarios = area / cobertura_por_litro
litros_necessarios *= 1.10

quantidade_latas = math.ceil(litros_necessarios / lata_litros)
custo_latas = quantidade_latas * preco_lata

quantidade_galoes = math.ceil(litros_necessarios / galao_litros)
custo_galoes = quantidade_galoes * preco_galao

# mistura latas e galoes
latas = int(litros_necessarios // lata_litros)
resto = litros_necessarios - (latas * lata_litros)
galoes = math.ceil(resto / galao_litros)

custo_mistura = latas * preco_lata + galoes * preco_galao

# Saída
print("-" * 40)
print("Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {quantidade_latas}")
print(f"Valor total: {custo_latas:.2f}")

print("-" * 40)
print("Comprar apenas galões de 3.6 litros")
print(f"Quantidade de galões: {quantidade_galoes}")
print(f"Valor total: {custo_galoes:.2f}\n")

print("-" * 40)
print("Comprar latas e galões:")
print(f"Latas: {latas}")
print(f"Galões: {galoes}")
print(f"Custo total: R$ {custo_mistura}")
print("-" * 40)
