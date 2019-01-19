def matriz(linhas, colunas):
    A = [[0 for x in range(colunas)] for y in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            A[i][j] = int(input())
    return A

def dimensao_matriz(A=[]):
    return len(A), len(A[0])

def somar_matrizes(A=[], B=[]):
    l, c = dimensao_matriz(A)
    S = [[0 for x in range(c)] for y in range(l)]
    for i in range(l):
        for j in range(c):
            S[i][j] = A[i][j] + B[i][j]
    return S

def multiplicar_matrizes(A=[], B=[]):
    l = dimensao_matriz(A)[0]
    c = dimensao_matriz(B)[1]
    M = [[0 for x in range(c)] for y in range(l)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                M[i][j] += A[i][k] * B[k][j]
    return M