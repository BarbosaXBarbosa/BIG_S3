def multiplicar(*args):
    s = 1
    for i in args:
        s *= i
    print(s)

multiplicar( 15, 20, 100)