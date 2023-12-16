import funcoes as f

f.dizerBomDia()
f.ehMultiplo(15, 45)
f.calcularBhaskara(2, -16, -18)

# Testando função string
palavra = input("Digite uma palavra:")
palavra_grande = f.palavraGrande(palavra)
if palavra_grande:
    print(f"Palavra {palavra} considerada grande.")
else:
    print(f"Palavra {palavra} não é considerada grande.")




