def codificador_hamming_palavra(palavra):
    v = palavra
    e = (v[0] + v[1] + v[2]) % 2
    f = (v[0] + v[1] + v[3]) % 2
    g = (v[0] + v[2] + v[3]) % 2

    v.append(e)
    v.append(f)
    v.append(g)
    return v

def codificador_hamming_frase(frase):
    num_palavras = len(frase) // 4
    frase_codificada = []
    for i in range(num_palavras):
        frase_codificada.extend(codificador_hamming_palavra(frase[4*i : 4*i + 4]))
    return frase_codificada

def hamming_codificar(frase):
    while len(frase) % 4:
        frase = to_int_array(input("Digite uma sequência válida! O tamanho da sequência deve ser um múltiplo de 4.\n"))
    return codificador_hamming_frase(frase)

def to_int_array(string):
    x = []
    for i in range(len(string)):
        x.append(int(string[i]))
    return x

def print_as_string(int_array):
    string = ''
    for i in int_array:
        string += str(i)
    print(string)

if __name__ == "__main__":
    vetor = to_int_array(input("Digite a sequência de bits a ser codificada.\n"))
    vetor_codificado = hamming_codificar(vetor)
    print("Sequência Codificada: ")
    print_as_string(vetor_codificado)
    pass