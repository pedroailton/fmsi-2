def exponencial(a, n):
    if a == 0 and n == 0:
        return "Impossível calcular."
    elif n < 0 :
        return "O expoente precisa ser positivo."
    elif n == 0:
        return 1
    else:
        return a * exponencial(a, n - 1)

a = float(input("Insira a base da potência: "))
n = int(input("Insira a potência a ser aplicada na base: "))
resultado = exponencial(a, n)

if isinstance(resultado, float): # isistance(), é a função verificadora de tipo
    print(f"Resultado: {resultado:.2f}") # se o resultado for do tipo "float", limite as casas devimais a 2
else: 
    print(f"Resultado: {resultado}")