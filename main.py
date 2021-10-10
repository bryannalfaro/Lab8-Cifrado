from functionsG import *
from modes import *
import pyDH
import hashlib
import base64

#PRIMERA PARTE
primo = 57
primo6digits = 131071
primo10digits = 2147483647
primo14digits = 67280421310721
g = generator(primo6digits)

#CLAVE PUBLICA
A = partition(g,primo6digits) # envia
B = partition(g,primo6digits) # envia


#print(A[1])
#print(B[1])

Ad = calculate(B[1],A[0],primo6digits)
Bd = calculate(A[1],B[0],primo6digits)

print('Clave: ',Ad==Bd)

#Segunda parte

d1 = pyDH.DiffieHellman() #Nosotros
d1_pubkey = d1.gen_public_key()
print('Clave publica: ',d1_pubkey)

d2_pubkey = int(input())

sharedkey = d1.gen_shared_key(d2_pubkey)
print('Clave compartida: ', sharedkey)


# sha256
plain_text = str(sharedkey)
text =  plain_text.encode('utf-8')
hash_sha256 = hashlib.sha256(text).digest()
print("Binario:\t", hash_sha256)

message = b"Hola! este es un mensaje de Julio"
print("Mensaje original: ", message)
cipher_text = EncryptCBC(message, hash_sha256)
print("Mensaje cifrado: ", cipher_text)

mensaje_a_descifrar = input()

recovered_message = DecryptCBC(mensaje_a_descifrar, hash_sha256)
print("Mensaje recuperado: ", recovered_message)