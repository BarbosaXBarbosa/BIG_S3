"""
1 – Crie uma função em Python que receba dois parâmetros: mensagem e quantidade.
O nome da função será imprimaMuitos().
A função imprimirá a mensagem passada por parâmetro quantas vezes foi informado
no parâmetro quantidade.
"""

def imprimaMuitos(msg, qtd):
    cont = 0
    while (cont < qtd):
        print(msg)
        cont += 1

def imprimaMuitosComFor(msg, qtd):
    for i in range(qtd):
        print(msg)
#######################################################
msg = input("Digite a mensagem:")
qtd = int(input("Digite a qtd de repetições:"))
imprimaMuitos(msg, qtd)
print("\n")
imprimaMuitosComFor(msg, qtd)





