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
