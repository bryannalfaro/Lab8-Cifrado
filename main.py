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

primo = primo14digits
g = generator(primo)

#CLAVE PUBLICA
A = partition(g,primo) # envia
B = partition(g,primo) # envia

#print(A[1])
#print(B[1])

Ad = calculate(B[1],A[0],primo)
Bd = calculate(A[1],B[0],primo)

print(f'\nCalculando primo = {primo}, de {len(str(primo))} digitos')
print('Clave A: ',Ad)
print('Clave B: ',Bd)
print('Igualdad: ',Ad==Bd)

input('\n\nPresione enter para continuar a la parte 2')
#Segunda parte

d1 = pyDH.DiffieHellman(15) #Nosotros
d1_pubkey = d1.gen_public_key()
print('\nMi clave publica: ',d1_pubkey)

d2_pubkey = int(input('\nIngrese la clave publica del otro usuario: '))

sharedkey = d1.gen_shared_key(d2_pubkey)
print('\nClave compartida: ', sharedkey)


# sha256
sharedkey = str(sharedkey)
plainText =  sharedkey.encode('utf-8')
hashKey = hashlib.sha256(plainText).digest()
print("\nHash 256 (Binario) de la clave compartida:\t", hashKey)

option = ''
while (option != 'salir'):
    option = input("\nIngrese la opcion: 'enviar', 'recibir' o 'salir': ")
    if option == 'enviar':
        message = input('\nIngrese el mensaje a cifrar: ')
        print("Mensaje original: ", message)
        cipher_text = EncryptCBC(message.encode('utf-8'), hashKey)
        print("Mensaje cifrado: ", cipher_text)

    if option == 'recibir':
        mensaje_a_descifrar = input('\nIngrese el mensaje a descifrar: ')

        recovered_message = DecryptCBC(mensaje_a_descifrar, hashKey)
        print("Mensaje recuperado: ", recovered_message)

    if option == 'salir':
        print('\nAdios')
