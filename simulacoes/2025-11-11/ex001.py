from random import randint

"""
n: número de dados
s: valor da soma dos valores obtidos
r: range (possibilidades possíveis)
"""

def gerarDados(n):
    """
    Recebe o número de dados
    Retorna uma lista com os valores sorteados
    """

    sorteios = []

    for i in range(0, n):
        sorteio = randint(1, n)
        sorteios.append(sorteio)

    return sorteios

def verificar(s, ref):
    """
    Recebe a soma
    Verifica se a soma é maior ou igual ao valor determinado (nessa questão é 12)
    """

    if s >= ref:
        return True
    else:
        return False

def operacaoSimples(n, ref):
    valores_sorteados = gerarDados(n)
    
    soma = sum(valores_sorteados)

    verificacao = verificar(soma, ref)

    if verificacao:
        print(f"O sorteio ultrapassou o valor {ref}")
        for i in valores_sorteados:
            print(f"Dado {i}: {valores_sorteados[i]}")
        print(f"Soma: {soma}")
    else:
        print(f"A soma não ultrapassou o valor {ref}")

def operacaoCompleta(n, ref, lancamentos):
    """
    Recebe o número de dados a serem lançados em um único lançamento
    Recebe o número de referência para comparação
    Recebe o número de lançamentos de dados que serão feitos

    Printa a media da porcentagem teórica

    Printa a media da porcentagem alcançada
    """
    resultados_desejados = []

    for i in range(0, lancamentos):
        valores_sorteados = gerarDados(n)

        soma = sum(valores_sorteados)

        verificacao = verificar(soma, ref)

        if verificacao:
            resultados_desejados.append(soma)

    ## média teórica
    media__porcentagem_teorica = (ref / (6 * n)) * 100
    print(f"Média da porcentagem calculada: {media__porcentagem_teorica}%")

    ## média calculada


def main():
    tipo = input("Qual o tipo de comparação (simples ou completa): ").strip().lower()
    n = int(input("Insira o número de dados a ser sorteado: "))
    ref = int(input("Insira o valor de comparação com a soma: "))

    if tipo == "simples":
        operacaoSimples(n, ref)
    elif tipo == "completa": 
        lancamentos = int(input("Insira quantos lançamentos deversão ser feitos: "))
        operacaoCompleta(n, ref, lancamentos)

if __name__ == "__main__":
    main()