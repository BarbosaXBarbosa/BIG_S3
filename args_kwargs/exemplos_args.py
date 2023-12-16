def multiplicarN(*args):
    s = 1
    for i in args:
        s *= i
    print(s)

def imprimirN(*nomes):
    for i in nomes:
        print(i)

if __name__ == "__main__":
    imprimirN("João", "Aline", "Gabriel")
    multiplicarN(10,20,30)