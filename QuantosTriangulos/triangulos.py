import matrizes as mt

def triangulos(A, B):
    existe_triangulo = False
    l, c = mt.dimensao_matriz(A)
    for i in range(l):
        for j in range(c):
            if(A[i][j] * B[i][j]):
                existe_triangulo = True
    return existe_triangulo

print("Digite a quantidade de vertices do grafo.")

vertices = int(input())

print("Informe matriz de adjacencia do grafo. Linha por linha.")

A = mt.matriz(vertices, vertices)

B = mt.multiplicar_matrizes(A, A)

if triangulos(A, B):
    print("Existe triangulo no grafo!")
else:
    print("Nao existe triangulo no grafo!")
