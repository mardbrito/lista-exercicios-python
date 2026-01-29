# Exercício 07
# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Informe o tamanho de um dos lados do quadrado: "))

area = lado * lado
dobro_area = area * 2

print(
    f"A área de um quadrado com o lado de {lado} é: {area} metros quadrados.")

print(f"O dobro da área é: {dobro_area} metros quadrados.")
