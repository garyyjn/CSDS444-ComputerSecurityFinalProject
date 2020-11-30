#import your algorithms here
from pip._vendor.distlib.compat import raw_input
from md5 import MD5_State
from RSA import xRsa
from VG import VG
from des import des
class Encryption_Runner:
    def __init__(self, algorithm = ''):
        self.algorithm = algorithm

    def run(self):
        if(self.algorithm == 'RSA'):
            print("Running RSA Encrption")
            msg = raw_input('Message: ')
            t = xRsa()
            print("plain text:" + msg)
            cipher = t.encrptyMsg(msg)
            print("cipher text:" + str(cipher))
        elif(self.algorithm == 'MD5'):
            print("Running MD5 Encrption")
            key = input("key:")
            obj = MD5_State()
            buff = [''] * 16
            ciper = obj.md5_digest(key, len(key), buff)
            print("deciper_text =")
            for i in range(16):
                print("%x" % ((ord(buff[i]) & 0xF0) >> 4), end='')
                print("%x" % (ord(buff[i]) & 0x0F), end='')
            #encryption = MD5()
        elif(self.algorithm == 'DES'):
            print("Running DES Encrption")
            desObj = des()
            desObj.encryption("key.txt", "file.txt")  # this will generte file(des).txt at the same directory
        elif(self.algorithm == 'VG'):
            print("Running VG Encrption")
            key = raw_input('key:')
            input_string = raw_input('input_string:')
            obj = VG()
            obj.create_table(key)
            print('key')
            print(obj.dict_key)
            print(obj.dict_char2int)
            print(obj.dict_int2char)
            print(obj.table)
            ciper_text = obj.cipher(input_string, key)
            print(ciper_text)
        else:
            print('END')
