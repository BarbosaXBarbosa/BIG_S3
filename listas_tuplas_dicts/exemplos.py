# Exemplos com listas
# 25/11/2023

# Criando uma lista

pets = ["Lulu", "Pingo", "Rex", "Nina"]

# Listas possuem índices:
# Imprimindo 1.° elemento:
print(pets[0])
# Imprimindo todos elementos:
print(pets)

# Dada a lista abaixo, faça um programa que receba um número inteiro
# e verifique se o número está contido na lista

# Criando lista:
numeros = [45, 78, 12, 44, 5, 8, 7, 0, -9, -8]
num = int(input("Digite um número:"))

if (num in numeros):
    print(f"{num} foi encontrado na lista!")
else:
    print(f"{num} não foi encontrado na lista!")

# Imprima o 4° elemento da lista do exemplo anterior:
print(numeros[3])

# Insira mais um elemento na lista e faça a soma de todos os elementos:
n = int(input("Digite um número para ser incluído na lista:"))
numeros.append(n)
# Realizando soma de todos números na lista:
print(f"Soma dos elementos da lista {numeros}\n {sum(numeros)}")

# Dicionários em Python

# Faça um cadastro de automóveis. O cadastro deve conter: Modelo, ano e valor
# A chave do dicionário será o nome do modelo e o valor será ano e valor.
# Fazer dois inputs de dados

# Criando dicionário:
carros = {}

modelo = input("Digite o modelo do carro:")
ano = int(input(f"Digite o ano do {modelo}:"))
valor = float(input(f"Digite o valor do {modelo} {ano}"))
# Adicionando elemento ao dicionário:
carros.update({modelo: [ano, valor]})
#
modelo = input("Digite o modelo do carro:")
ano = int(input(f"Digite o ano do {modelo}:"))
valor = float(input(f"Digite o valor do {modelo} {ano}"))
carros.update({modelo: [ano, valor]})
# Saída de dados:
keys = list(carros.keys())
# keys = [corolla, uno, fusca, jetta]
print(f" Modelo: {keys[0]} | Ano: {carros[keys[0]][0]}"
      f" | Valor: {carros[keys[0]][1]}")
print(f" Modelo: {keys[1]} | Ano: {carros[keys[1]][0]}"
      f" | Valor: {carros[keys[1]][1]}")

