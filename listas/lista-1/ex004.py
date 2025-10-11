def mdc(a, b):
    if a == 0 and b == 0:
        return "mdc indeterminado"
    elif b == 0: # Caso base
        return a
    else:
        return mdc(b, a % b)
    
a = int(input("Insira o primeiro número para a operação: "))
b = int(input("Insira o segundo número para a operação: "))
resultado = mdc(a, b)
print(f"O resultado é: {resultado}")