import random

def codificador_hamming_palavra(vetor_palavra):
    v = vetor_palavra
    e = (v[0] + v[1] + v[2]) % 2
    f = (v[0] + v[1] + v[3]) % 2
    g = (v[0] + v[2] + v[3]) % 2
    
    v.append(e)
    v.append(f)
    v.append(g)
    return v

def codificador_hamming_frase(vetor_frase):
    num_palavras = len(vetor_frase)/4
    frase_codificada = []
    for i in range(0, int(num_palavras)):
        frase_codificada.append(codificador_hamming_palavra(vetor_frase[4*i : 4*i + 4]))
    return frase_codificada

def hamming_codificar(vetor_frase):
    while(len(vetor_frase) % 4 != 0):
        vetor_frase = to_int_array(input("Digite uma sequência válida! O tamanho da sequência deve ser um múltiplo de 4.\n"))
    vetor_frase = codificador_hamming_frase(vetor_frase)
    print("Sequência codificada: ")
    print_as_string(vetor_frase)
    return vetor_frase

def hamming_inserir_erro_palavra(vetor_palavra, num_erro):
    for i in range(num_erro):
        idx = random.randint(0, 6)
        vetor_palavra[idx] = str((int(vetor_palavra[idx]) + 1) % 2)
    return vetor_palavra

def hamming_inserir_erro_frase(vetor_frase, num_erro):
    num_palavras = len(vetor_frase)/7
    frase_errada = ""
    for i in range(0, int(num_palavras)):
        frase_errada = frase_errada + str(hamming_inserir_erro_palavra(vetor_frase[7*i : 7*i + 7], num_erro))
    return frase_errada

def hamming_decodificar(vetor_frase):
    return

def to_int_array(string):
    x = []
    for i in range(len(string)):
        x.append(int(string[i]))
    return x

def print_as_string(int_array):
    string = ''
    for i in int_array:
        string = string + str(i)
    print(string)

if __name__ == "__main__":
    vec = to_int_array(input("Digite a sequência de bits a ser codificada.\n"))
    code_vec = hamming_codificar(vec)
    #hamming_inserir_erro_frase(code_vec, num_erro=1)
    #hamming_decodificar(code_vec)
    pass