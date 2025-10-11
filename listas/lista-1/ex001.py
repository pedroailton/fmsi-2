def fatorial(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
n = int(input("Entrada: "))
print(f"Fatorial da entrada {fatorial(n)}")