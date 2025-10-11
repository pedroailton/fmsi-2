def exponencialModular(a, n, m):
    if a == 0 and n == 0:
        return "impossível calcular"
    elif m <= 1:
        return "impossível calcular"
    elif n < 0:
        return "expoente negativo não aceito"
    else:
        if n == 0: # caso base
            return 1
        if n % 2 == 0: # se n for par
            metade =  exponencialModular(a, n//2, m)
            return (metade * metade) % m
        else: # se n for ímpar
            return (a * exponencialModular(a, n - 1, m)) % m

a = float(input("Insira a base: "))
n = int(input("Insira o expoente: "))
m = int(input("Insira o módulo: "))

print(exponencialModular(a, n, m))
