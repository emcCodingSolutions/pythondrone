from  Crypto.Cipher import AES
from  Crypto.Util.Padding import pad
from base64 import b64encode

key = input('Please input password: ')
# encode UTF-8 the key and into bytes
key = key.encode('UTF-8')
key = pad(key)

# Encryption function
def encrypt (file_name, key):
    with open(file_name, 'rb') as entry:
        data = entry.read() 
        cipher = AES.new(key, AES.MODE_CFB)
            ciphertext = cipher.exctypt(pad(data, AES.block_size))
            iv = b64encode(cipher.iv).decode('UTF-8')
            ciphertext = b64(ciphertext).decode('UTF-8')
            to_write = iv + ciphertext
        entry.close()
        with open(filename + '.enc', 'w') as data:
            data.write(to_write)
        data.close()
            


encrypt('sample.mp4', key)
