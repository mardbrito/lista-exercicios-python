# Exercício 13
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

# Para Megabytes: Gigabytes * 1024
# Para Kilobytes: Gigabytes * 1024 * 1024
# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

tamanho = int(input("Informe o tamanho do arquivo em Gigabytes: "))

megabytes = tamanho * 1024
kilobytes = tamanho * 1024 * 1024

print(
    f"O tamanho desse arquivo de {tamanho} gigabytes equivale a:\n\t {megabytes} megabytes\n\t {kilobytes} kilobytes")
