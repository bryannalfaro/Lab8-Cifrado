from functionsG import *
import pyDH

#PRIMERA PARTE
primo = 57
g = generator(primo)

#CLAVE PUBLICA
A = partition(g,primo) # envia
B = partition(g,primo) # envia


print(A[1])
print(B[1])

Ad = calculate(B[1],A[0])
Bd = calculate(A[1],B[0])

print('Clave: ',Ad)
print('Clave: ',Bd)

#Segunda parte

d1 = pyDH.DiffieHellman() #Nosotros
d2 = pyDH.DiffieHellman()
d1_pubkey = d1.gen_public_key()
d2_pubkey = d2.gen_public_key()
d1_sharedkey = d1.gen_shared_key(d2_pubkey)
d2_sharedkey = d2.gen_shared_key(d1_pubkey)
print(d1_sharedkey == d2_sharedkey)