# Exercício 04
# Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota_um = int(input("Informe a primeira nota: "))
nota_dois = int(input("Informe a segunda nota: "))
nota_tres = int(input("Informe a terceira  nota: "))
nota_quatro = int(input("Informe a quarta nota: "))

media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

print("A média das notas informadas é:", media)
