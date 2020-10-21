import argparse
from Decryption_Runner import Decryption_Runner
from Encryption_Runner import Encryption_Runner

parser = argparse.ArgumentParser(description="Encryption/Decryption Runnner")
parser.add_argument('-m', action='store', dest = 'mode', help = 'encrypt/decrypt')
parser.add_argument('-a', action='store', dest = 'algorithm')


args = parser.parse_args()

if(args.mode == 'encrypt'):
    encryptor = Encryption_Runner(args.algorithm)
    encryptor.run()
elif(args.mode == 'decrypt'):
    decrytor = Decryption_Runner(args.algorithm)
    decrytor.run()