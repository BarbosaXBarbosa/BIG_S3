"""
1 – Crie um programa em Python que atribua dois nomes e duas idades em variáveis
separadas. Mostre a seguinte informação em tela para os dois casos:
"Nome1 tem idade1 anos".
"""
nome1 = "João"
nome2 = "Isabella"
idade1 = 18
idade2 = 20
print(f"{nome1} tem {idade1} anos ")
print(f"{nome2} tem {idade2} anos ")

"""
2 – Crie um programa em Python que receba 3 notas de um aluno (de 0.0 até 10.0).
Mostre na tela qual o valor da média aritmética do aluno e se o aluno foi 
aprovado ou não, sabendo que a regra de aprovação é média >= 7.5.
"""
n1 = float(input("Digite a 1° nota"))
n2 = float(input("Digite a 2° nota"))
n3 = float(input("Digite a 3° nota"))

media = (n1 + n2 + n3) / 3
passou = media >= 7.5

print(f"Nota final: {media:.2f}")
if passou:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")





