"""
1 – Crie uma lista manual em Python contendo três valores string que você
desejar.
Mostre na tela quantos elementos a lista tem.
Adicione mais dois elementos através da função input() usando o método append().
Mostre novamente quantos elementos tem na lista.
"""
carros = ["Gol", "Fusca", "Corolla"]
print(f"Qtd inicial de elementos: {len(carros)}")
carro1 = input("Digite o nome de um carro")
# Adicionando elemento na lista
carros.append(carro1)
carro2 = input("Digite o nome de outro carro")
carros.append(carro2)
print(carros)
print(f"Qtd final de elementos: {len(carros)}")

"""
2 – Crie um dicionário de dados em Python com os seguintes valores: 
"Nome do produto", quantidade e valor unitário.
O nome do produto será a chave e a quantidade e valor serão uma lista.
Inserir dois produtos no dicionário através de dados vindos da função input()
Mostre os produtos cadastrados na tela: Nome, quantidade, valor e o 
valor total em estoque, sem usar estrutura de repetição.
"""
print(f"\nAtividade 2\n")
produtos = {}

# Input de dados:
nome = input("Digite o nome do produto:")
qtd = float(input(f"Digite a qtd do {nome}:"))
valor = float(input(f"Digite o valor do {nome}:"))
# produtos[nome] = [qtd, valor]
produtos.update({nome: [qtd, valor]})
# 2° Produto:
nome = input("Digite o nome do produto:")
qtd = float(input(f"Digite a qtd do {nome}:"))
valor = float(input(f"Digite o valor do {nome}:"))
# produtos[nome] = [qtd, valor]
produtos.update({nome: [qtd, valor]})
# Mostrando valores em tela:
# [iphone, galaxy s23+, moto g43]
keys = list(produtos.keys())
print(f"{keys[0]:12} | Qtd: {produtos[keys[0]][0]:5} | "
      f"Vlr_unit: {produtos[keys[0]][1]:7} | "
      f"Total: {produtos[keys[0]][0] * produtos[keys[0]][1]:,.2f}")

print(f"{keys[1]:12} | Qtd: {produtos[keys[1]][0]:5} | "
      f"Vlr_unit: {produtos[keys[1]][1]:7} | "
      f"Total: {produtos[keys[1]][0] * produtos[keys[1]][1]:,.2f}")

total_estoque = (produtos[keys[0]][0] * produtos[keys[0]][1]) + (produtos[keys[1]][0] * produtos[keys[1]][1])
print(f"\nEstoque total: {total_estoque:,.2f}")



