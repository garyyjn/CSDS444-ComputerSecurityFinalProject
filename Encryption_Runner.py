#import your algorithms here

class Encryption_Runner:
    def __init__(self, algorithm = ''):
        self.algorithm = algorithm

    def run(self):
        if(self.algorithm == 'RSA'):
            print("Running RSA Encrption")
            #encryption = RSA()
        if(self.algorithm == 'MD5'):
            print("Running MD5 Encrption")
            #encryption = MD5()
        if(self.algorithm == 'DES'):
            print("Running DES Encrption")
            #encryption = DES()

