from random import randrange
def generator(primo):
    g = randrange(2,primo-1)
    return g

def partition(g,primo):
    value =  randrange(2,primo-1)
    return value,(g**value)%primo

def calculate(base, value,primo):
    return (base**value)%primo

def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result