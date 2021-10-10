from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def EncryptCBC(data, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = b64encode(iv+ct_bytes).decode('utf-8')
    result = ct
    return result

def DecryptCBC(result, key):
    cipher = AES.new(key, AES.MODE_CBC, b64decode(result)[:AES.block_size])
    pt = unpad(cipher.decrypt(b64decode(result)[AES.block_size:]), AES.block_size)
    return pt
