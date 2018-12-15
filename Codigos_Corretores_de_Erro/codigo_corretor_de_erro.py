from Codigos_Corretores_de_Erro import codificador_hamming as ch
from Codigos_Corretores_de_Erro import insersor_de_erro as ie
from Codigos_Corretores_de_Erro import decodificador_hamming as dh

def as_array(string):
    x = []
    for i in range(len(string)):
        x.append(int(string[i]))
    return x

def as_string(array):
    string = ''
    for i in array:
        string += str(i)
    return string

frase = as_array(input("Digite a sequência binária a ser codificada.\n"))

while len(frase) % 4:
    frase = as_array(input("Digite uma sequência válida! O tamanho da sequência deve ser um múltiplo de 4.\n"))

frase_codificada = ch.codificador_hamming_frase(frase)
print("Frase Codificada:\n" + as_string(frase_codificada))

frase_errada = ie.hamming_inserir_erro_frase(frase_codificada, 1)
print("Inserindo, no máximo, 1 erro aleatório por palavra:\n" + as_string(frase_errada))

frase_decodificada = dh.hamming_decodificar_frase(frase_errada)
print("Frase Decodificada:\n" + as_string(frase_decodificada))