from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode


key = input ('Input your password: ')
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

def encrypt (fileName, key):
    with open(fileName, 'rb') as entry:
        data = entry.read()
        cipher = AES.new(key, AES.MODE_CFB)
        cipherText = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('UTF-8')
        
        cipherText = b64encode(cipherText).decode('UTF-8')
        to_write = iv + cipherText
    entry.close()
    with open(fileName + '.enc', 'w') as data:
        data.write(to_write)
    data.close()

encrypt('sample.mp4', key)
# encrypt('test.txt', key)
