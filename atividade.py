"""
Aluno: Pedro Ailton Alves da Cunha (trabalho feito sozinho)
TUrma: 2º Período de Bacharelado em Sistemas de Informação
Atividade: Simulação de completar álbuns de figurinhas
"""

import random as rd

# Etapa 1: Gerar Dados
def abrirPacote(num_max):
    figurinhas_do_pacote = []
    for _ in range(5):
        figurinhas_do_pacote.append(rd.randint(1, num_max))
    return figurinhas_do_pacote
    
# Etapa 2: Teste
def verificarAutenticidade(figurinha, album):
    return not figurinha in album

# Etapa 3: 1 Simulação
def completar1Album(num_max):
    album = [None] * num_max # cria uma lista com num_max posições ocupadas por None
    qtd_pacotes_abertos = 0

    while None in album:
        figurinhas_do_pacote = abrirPacote(num_max)

        qtd_pacotes_abertos += 1

        for figurinha in figurinhas_do_pacote:
            if verificarAutenticidade(figurinha, album):
                album[figurinha - 1] = figurinha # a posição é menor em 1, uma vez que a lista album possui índices que começam em 0

    return qtd_pacotes_abertos

# Etapa 4: Várias simulações
def completarVariosAlbuns(num_max, qtd_albuns):
    qtd_pacotes_abertos_total = 0
    for _ in range(qtd_albuns):
        qtd_pacotes_abertos_total += completar1Album(num_max)

    media = qtd_pacotes_abertos_total / qtd_albuns

    return media

num_max = 500 # chamado de n no enunciado
num_albuns = 200 # chamado de N no enunciado

# Rodando o programa
print('Simulação de completar álbuns de figurinhas:')
resultado = completar1Album (num_max)
print(f'Foram abertos {resultado} pacotes para completar o álbum de {num_max} figurinhas.')

print('\nSimulação de completar vários álbuns de figurinhas:')
resultado_varios = completarVariosAlbuns(num_max, num_albuns)
print(f'Em média, foram abertos {resultado_varios} pacotes para completar {num_albuns} álbuns de {num_max} figurinhas.')
print(f'(de maneira realista, serão necessários abrir {(resultado_varios // 1) + 1:.0f} pacotes para completar um álbum de {num_max} figurinhas)')