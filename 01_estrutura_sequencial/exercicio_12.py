# Exercício 12
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

# Formula: Gigabytes * 1024

tamanho = int(input("Informe o tamanho do arquivo em Gigabytes: "))

megabytes = tamanho * 1024

print(
    f"O tamanho desse arquivo de {tamanho} gigabytes equivale a\n\t {megabytes} megabytes.")
