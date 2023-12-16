"""
1 – Crie uma lista manualmente com 5 elementos (cada elemento será uma lista
contendo código e valor. Ex: [[1,"SENAI"],[2,"SESI"], etc].
Mostre todos os valores da lista usando o comando for.
"""
print("Atividade 1")
carros = [[1, "Yaris"],[2, "Gol"],[3, "Sentra"],[4, "Civic"],[5, "Marea"]]
for carro in carros:
    print(f"Codigo: {carro[0]} | Modelo: {carro[1]}")

"""
2 – Crie um programa que receba dois valores para cálculo de uma exponenciação.
O primeiro valor será a base e o segundo valor a quantidade de repetições.
Para cada repetição a seguinte fórmula será executada: x = x + base^2.
Mostre, a cada repetição, o valor de x. A repetição deve ser feita usando o 
comando while.
"""
print("Atividade 2")
base = int(input("Digite o valor da base:"))
qtd = int(input("Digite a qtd de repetições:"))
cont = 0
x = 0
while (cont < qtd):
    x += base ** 2  # x = x + base ** 2
    print(x)
    cont += 1

