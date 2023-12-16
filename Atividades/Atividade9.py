def mediaNotas(*notas):
    s = 0
    for n in notas:
        s += n
    media = s / len(notas)
    print(f"Média: {media}")

def calcularMedia():
    entrada_notas = input("Insira as notas do aluno separadas por vírgula: ")
    notas = [float(nota) for nota in entrada_notas.split(",")]
    mediaNotas(*notas)

calcularMedia()