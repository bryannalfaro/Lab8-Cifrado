from functionsG import *
from modes import *
import pyDH
import hashlib
import base64

#PRIMERA PARTE
primo = 57
primo6digits = 131071
primo10digits = 1190494759
primo14digits = 67280421310721
g = generator(primo10digits)

#CLAVE PUBLICA
A = partition(g,primo14digits) # envia
B = partition(g,primo14digits) # envia

#print(A[1])
#print(B[1])

Ad = calculate(B[1],A[0],primo14digits)
Bd = calculate(A[1],B[0],primo14digits)

print('Clave A: ',Ad)
print('Clave B: ',Bd)
print('Igualdad: ',Ad==Bd)

#Segunda parte

d1 = pyDH.DiffieHellman(15) #Nosotros
d1_pubkey = d1.gen_public_key()
print('Clave publica: ',d1_pubkey)

d2_pubkey = int(input())

sharedkey = d1.gen_shared_key(d2_pubkey)
print('Clave compartida: ', sharedkey)


# sha256
sharedkey = str(sharedkey)
plainText =  sharedkey.encode('utf-8')
hashKey = hashlib.sha256(plainText).digest()
print("Binario:\t", hashKey)

option = ''
while (option != 'salir'):
    print("Ingrese la opcion: 'enviar' o 'recibir'")
    option = input()
    if option == 'enviar':
        message = input('Ingrese el mensaje a cifrar: ')
        print("Mensaje original: ", message)
        cipher_text = EncryptCBC(message.encode('utf-8'), hashKey)
        print("Mensaje cifrado: ", cipher_text)

    if option == 'recibir':
        mensaje_a_descifrar = input('Ingrese el mensaje a descifrar: ')

        recovered_message = DecryptCBC(mensaje_a_descifrar, hashKey)
        print("Mensaje recuperado: ", recovered_message)

