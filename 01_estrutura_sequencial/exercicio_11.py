# Exercício 11
# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

numero_1 = int(input("Informe um número inteiro: "))
numero_2 = int(input("Informe outro número inteiro: "))
numero_3 = float(input("Informe um número real: "))

produto = numero_1 * 2 * numero_2 / 2
soma = numero_1 * 3 + numero_3
cubo = numero_3 ** 3

print("*" * 20)
print(
    f"O produto do dobro do primeiro com metade do segundo: {produto}")
print(
    f"A soma do triplo do primeiro com o terceiro: {soma}")
print(f"O terceiro elevado ao cubo: {cubo}")
print("*" * 20)
