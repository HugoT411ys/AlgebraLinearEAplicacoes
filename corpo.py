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
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    n = int(input("Enter n: "))
    s = (a + b) % n
    p = (a * b) % n
    print(str(a) + " + " + str(b) + " modulo " + str(n) + " is: " + str(s))
    print(str(a) + " * " + str(b) + " modulo " + str(n) + " is: " + str(p))

    if is_prime(n):
        print("Z_" + str(n) + " is a field.")
    else:
        print("Z_" + str(n) + " is not a field.")

def main():
    field()

if __name__ == '__main__':
    main()