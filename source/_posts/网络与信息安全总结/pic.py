from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time
from PIL import Image

class crypt():
    def to32(self, text):
        length = 32
        count = len(text)
        if(count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        if(type(text) is str):
            text = text + ('\0'*add)
        elif(type(text) is bytes):
            text = text + (b'\00'*add)
        else:
            pass
        return text

    def __init__(self, key):
        self.key = self.to32(key).encode('utf8')
        self.mode = AES.MODE_CBC
        self.cryptor = AES.new(self.key, self.mode)

    def readPic(self, path):
        f = open(path, 'rb')
        filedata = f.read()
        f.close()
        return filedata

    def convert_to_RGB(self, data):
        r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2]))
        pixels = tuple(zip(r,g,b))
        return pixels

    def encrypt(self, path):
        im = Image.open(path)
        data = im.convert("RGB").tobytes() 
        ciphertext = self.cryptor.encrypt(self.to32(data))
        # new pic
        original = len(data) 
        new = self.convert_to_RGB(ciphertext[:original]) 
        #print(new)
        im2 = Image.new(im.mode,im.size)
        im2.putdata(new)
        im2.save("encrypted"+"."+"bmp", "bmp")
        return "succeed"

    def decrypt(self, text):
        plain_text = self.cryptor.decrypt(a2b_hex(text))
        return plain_text

if __name__ == '__main__':
    starttime = time.clock()
    c = crypt("keykeykeykey")
    e = c.encrypt('./pic.bmp')
    endtime = time.clock()
    print(e, "time:", (endtime-starttime)*10000)