import numpy as np

def matriz_checagem_paridade():
    return np.array([[1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 1]])

def processar_erro(v, P, palavra):
    if(v[0] == 0 and v[1] == 0 and v[2] == 0):
        return palavra
    else:
        i = indice_coluna(v, P)
        palavra[i] = (palavra[i] + 1) % 2
        return palavra

def indice_coluna(v, P):
    for i in range(7):
        if(v[0] == P[0][i] and v[1] == P[1][i] and v[2] == P[2][i]):
            return i

def hamming_decodificar_palavra(palavra):
    P = matriz_checagem_paridade()
    coluna_erro = P.dot(palavra)
    coluna_erro = coluna_erro % 2
    palavra = processar_erro(coluna_erro, P, palavra)
    return palavra[0 : 4]

def hamming_decodificar_frase(frase):
    num_palavras = len(frase) // 7
    frase_decodificada = []
    for i in range(num_palavras):
        frase_decodificada.extend(hamming_decodificar_palavra(frase[7*i : 7*i+7]))
    return frase_decodificada