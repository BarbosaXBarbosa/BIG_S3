# 02/12/2023
# Criando funções em Python
import math as mt

def dizerBomDia():
    print("Bom dia!")

# Crie uma função que verifique se um número é múltiplo de outro:
def ehMultiplo(a, b):
    if (a % b == 0):
        print(f"{a} é múltiplo de {b}")
    else:
        print(f"{a} não é múltiplo de {b}")


def palavraGrande(palavra):
    if (len(palavra) >= 10):
        return True
    else:
        return False

# Crie uma função que calcule a fórmula de Bhaskara

def calcularBhaskara(a, b, c):
    delta = b ** 2 - (4 * a * c)
    x1 = (- b + mt.sqrt(delta)) / (2 * a)
    x2 = (- b - mt.sqrt(delta)) / (2 * a)
    print(f"Valor de delta = {delta}")
    print(f"Valor de x' = {x1:.2f}")
    print(f"Valor de x'' = {x2:.2f}")

# Testando funções:
if (__name__ == "__main__"):
    dizerBomDia()
    ehMultiplo(480, 40)


