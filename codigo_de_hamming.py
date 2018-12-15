
'''

codigo de Hamming:

 abcd -> abcdefg, e = a + b + c,
                  f = b + c + d,
                  g = a + c + d
'''

def codificar(msg):
    print('Mensagem: ' + msg)
    e = (int(msg[0]) + int(msg[1]) + int(msg[2])) % 2
    f = (int(msg[1]) + int(msg[2]) + int(msg[3])) % 2
    g = (int(msg[0]) + int(msg[2]) + int(msg[3])) % 2

    return msg + str(e) + str(f) + str(g)

entrada = input('Digite a sequencia: ')

if(len(entrada) % 4 != 0):
    print("Sequencia invalida!")
    exit(0)
else:
    print('Sequencia valida')

    print(str(len(entrada)) + ' digitos')

    for i in range(len(entrada)//4):
        print(codificar(entrada[4*i : 4*i + 4]))