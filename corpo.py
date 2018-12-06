import numpy as np

def is_prime(number):
    sq_root = int(np.sqrt(number))
    for i in range(2, sq_root+1):
        if number % i == 0:
            return False
        else:
            i += 1
    return True

def field():
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))
    n = int(input("Valor de c: "))
    s = (a + b) % n
    p = (a * b) % n
    print(str(a) + " + " + str(b) + " modulo " + str(n) + " eh: " + str(s))
    print(str(a) + " * " + str(b) + " modulo " + str(n) + " eh: " + str(p))

    if is_prime(n):
        print("Z/" + str(n) + "Z " + " eh um corpo.")
    else:
        print("Z/" + str(n) + "Z " + " eh um corpo.")

def main():
    field()

if __name__ == '__main__':
    main()
