#import your algorithms here
from pip._vendor.distlib.compat import raw_input
from md5 import MD5_State
from RSA import xRsa
from VG import VG
from des import des
class Decryption_Runner:
    def __init__(self, algorithm=''):
        self.algorithm = algorithm

    def run(self):
        if(self.algorithm == 'RSA'):
            t = xRsa()
            print("Running RSA Decryption")
            cipher = raw_input("Cipher text: ")
            plaintext = t.decrptyMsg(cipher)
            # Print the string content after encryption and decryption
            print("decrypted text:" + plaintext)
        elif(self.algorithm == 'MD5'):
            print("unsupported")
        elif(self.algorithm == 'DES'):
            print("Running DES Decryption")
            desObj = des()
            desObj.decryption("key.txt", "file(txt).des")  # thie will generate file.txt at the same directory
        elif (self.algorithm == 'VG'):
            print("Running VG Decryption")
            obj = VG()
            cipher_text = input("Cipher_text: ")
            key = input("Key: ")
            deciper_text = obj.decipher(cipher_text, key)
            print(deciper_text)
        else:
            print("end")