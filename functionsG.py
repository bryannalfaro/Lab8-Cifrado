from random import randrange
def generator(primo):
    g = randrange(2,primo-1)
    return g

def partition(g,primo):
    value =  randrange(2,primo-1)
    return value,g**value

def calculate(base, value):
    return base**value