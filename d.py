from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
# This a dead import
# import getpass

# key = getpass.getpass('Please enter your password: ')
key = input('Input your password: ')
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

# with open('test.txt.enc', 'r') as entry:
with open('sample.mp4.enc', 'r') as entry:
    try:
        data = entry.read()
        length = len(data)
        
        # iv is the initialization factor
        iv = data[:24]
        iv = b64decode(iv)
        ciphertext = data[24:length]
        ciphertext = b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CFB, iv)

        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted, AES.block_size)
        
        #  Write all this to a new file
        with open ('sample_un.mp4', 'wb') as data:
            data.write(decrypted)
        data.close()
    except(ValueError, KeyError):
        print('Wrong password.')




# Works with .jpg files as well

# Change -> encrypt('test.txt', key)
# to -> encrypt('myfile.jpg', key)
# in the encrypt.py

# Also here, change -> ('test.txt.enc', 'r') as entry:
# to ('myfile.jpg.enc', 'r') as entry:

# and -> with open ('testunencrypted.txt', 'wb') as data:
# to -> ('decrypted.jpg', 'wb') as data: