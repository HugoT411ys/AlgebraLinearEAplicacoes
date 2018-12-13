import random

def hamming_inserir_erro_palavra(palavra, num_erro):
    for i in range(num_erro):
        random_pos = random.randint(0, 6)
        palavra[random_pos] = (palavra[random_pos] + 1) % 2
    return palavra

def hamming_inserir_erro_frase(frase, num_erro):
    num_palavras = len(frase) // 7
    frase_errada = []
    for i in range(num_palavras):
        frase_errada.extend(hamming_inserir_erro_palavra(frase[7*i : 7*i + 7], num_erro))
    return frase_errada

def hamming_inserir_erro(frase):
    while len(frase) % 7:
        frase = to_int_array(input("Digite uma sequência válida! O tamanho da sequência deve ser um múltiplo de 7.\n"))
    return hamming_inserir_erro_frase(frase, 1)

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
    vetor = to_int_array(input("Digite a sequência de bits na qual o erro será inserido.\n"))
    vetor_errado = hamming_inserir_erro(vetor)
    print("Sequência Errada: ")
    print_as_string(vetor_errado)
    pass