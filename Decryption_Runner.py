#import your algorithms here

class Decryption_Runner:
    def __init__(self, algorithm=''):
        self.algorithm = algorithm

    def run(self):
        if(self.algorithm == 'RSA'):
            print("Running RSA Decryption")
        if(self.algorithm == 'MD5'):
            print("Running MD5 Decryption")
        if(self.algorithm == 'DES'):
            print("Running DES Decryption")