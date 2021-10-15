from random import randrange
import numpy as np
def generator(primo):
    g = randrange(2,primo-1)
    return g

def partition(g,primo):
    value =  randrange(2,primo-1)
    return value,pow(g,value,primo)

def calculate(base, value,primo):
    return pow(base,value,primo)

def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result

def testFermat(n,k):
    prime = True
    pruebas = []
    for i in range(0,k):
        a = np.random.randint(2,n-2,dtype=np.int64)
        pruebas.append(a)
        if (binpow(a,n-1)%n)!=1:
            prime = False
    if prime:
        return prime,pruebas
    else:
        return prime,a

def generatorPrimes(longitud, cantidad):
    numb = '1'+(longitud-1)*'0'
    numb = int(numb)
    print(numb)
    print(numb*100)
    primos = []
    while len(primos) < cantidad:
        numero = np.random.randint(numb, numb*100,dtype=np.int64)
        if testFermat(numero,5)[0]==True:
            print('Se genero un primo ')
            primos.append(numero)
        else:
            pass

    return primos