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
