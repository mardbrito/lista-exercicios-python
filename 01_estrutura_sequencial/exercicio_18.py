# Exercício 18
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Tamanho do arquivo para download (MB): "))
link = float(input("Velocidade do link (Mbps): "))

tempo_aproximado = tamanho / link

print(
    f"O tempo para o download desse arquivo será aproximadamente: {tempo_aproximado / 60:.2f}")
