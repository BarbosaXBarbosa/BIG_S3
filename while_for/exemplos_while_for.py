# 02/12/2023
# Exemplos com while e for
import time

# Crie um programa que repita 15 vezes a palavra boa tarde.

# Criando uma variável contadora
cont = 1
while (cont <= 15):
    print(f"Repetição {cont}: Boa tarde!")
    # Incrementando variável contadora
    cont += 1  # cont = cont + 1

# Crie um programa que faça um cadastro de pets.
# No cadastro deve conter: nome do pet, idade e espécie.
# Cada pet deve ser armazenado em uma lista.
# O usuário irá finalizar o cadastro quando digitar "0" no nome do pet.
# Ao final mostre todos os pets cadastrados e a quantidade.
# Mostre também somente os pets que possuem 10 anos ou mais como "Pets idosos":
print("Cadastro de Pets\n")
pets = []
cont = 1
while True:
    nome = input(f"Digite o nome do {cont}° pet:")
    if (nome == "0"):
        break
    idade = int(input(f"Digite a idade do (a) {nome}:"))
    especie = input(f"Digite a espécie do (a) {nome}")
    pets.append([nome, idade, especie])
    cont += 1
# ["Lulu", 4, "cachorro"]
# Mostrando cadastro dos pets na tela:
pets_idosos = []
print(f"\nPets cadastrados:\n")
for i in pets:
    if (i[1] >= 10):  # Se o pet for idoso, iremos adicioná-lo na nova lista:
        pets_idosos.append(i)
    print(f"Nome: {i[0]:12} | Idade: {i[1]:2} | Espécie: {i[2]}")
print(f"\nQtd de pets cadastrados: {len(pets)}")
#
# Verificando se a lista de pets idosos está vazia ou não:
if pets_idosos:
    print(f"\nPets idosos:")
    for i in pets_idosos:
        print(f"Nome: {i[0]:12} | Idade: {i[1]:2} | Espécie: {i[2]}")

# Usando dicionários em Python

# Crie um programa que faça um cadastro de empresas
# Deve conter as seguintes informações:
# Nome, cnpj, estado matriz / filial
# As empresas deverão ser cadastradas em um dicionário cuja chave será
# O nome da empresa. Exemplo: "Empresa X": [00000, "SP"]
# O cadastro deve ser finalizado quando o usuário digitar "0" no nome da empresa.
# Ao final mostre quantas empresas de SP foram cadastradas.
print("Cadastro de empresas\n")
# Criando dicionário:
empresas = {}
cont = 1
contsp = 0
while True:
    nome = input(f"Digite o nome da {cont}° empresa:")
    if (nome == "0"):
        break
    cnpj = input(f"Digite o CNPJ da empresa {nome}:")
    uf = input(f"Digite o estado da empresa {nome}:")
    # Adicionando elemento no dicionário:
    empresas.update({nome: [cnpj, uf]})
    # empresas[nome] = [cnpj, uf]
    if (empresas[nome][1].lower() == "sp"):
        # Se a empresa for de SP o contador contsp é incrementado:
        contsp += 1  # contsp = contsp + 1
    cont += 1  # Incrementando contador geral

# Exibindo empresas cadastradas:
print(f"\nEmpresas cadastradas\n")
for c, v in empresas.items():
    print(f"Empresa: {c:15} | CNPJ: {v[0]:14} | UF: {v[1]}")
#
if contsp > 0:
    print(f"\nForam cadastradas {contsp} empresas de São Paulo.")
else:
    print("\nNenhuma empresa de São Paulo cadastrada.")


