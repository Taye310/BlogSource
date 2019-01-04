from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time

class crypt():
    def to32(self, text):
        length = 32
        count = len(text)
        if(count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0'*add)
        return text

    def __init__(self, key):
        self.key = self.to32(key).encode('utf8')
        self.mode = AES.MODE_CBC
        self.cryptor = AES.new(self.key, self.mode)

    def encrypt(self, text):
        self.ciphertext = self.cryptor.encrypt(self.to32(text).encode('utf8'))
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        plain_text = self.cryptor.decrypt(a2b_hex(text))
        return plain_text


if __name__ == '__main__':
    starttime = time.clock()
    c = crypt("keykeykeykeykeykey")
    e = c.encrypt("0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef")
    # d = c.decrypt(e)
    endtime = time.clock()
    print(e, "time:", (endtime-starttime)*10000)
