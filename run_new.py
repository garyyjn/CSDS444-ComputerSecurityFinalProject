from VG import VG
from RSA import xRsa
from des import des
from md5 import MD5_State
import string
import sys

from pip._vendor.distlib.compat import raw_input

while True:
    input = raw_input('exit or work:')
    if input == 'exit':
        exit()
    elif input == 'work':
        type  = raw_input("Select method(vg,des,rsa,md5):")
        if type == 'vg':
            vg_1 = VG()
            key = raw_input('key:')
            plain_text = raw_input('plain_text:')
            table = vg_1.create_table(key)
            print("Table created!")
            print(table)
            cipher_text = vg_1.cipher(plain_text,key)
            print("Encrypted finish")
            print(cipher_text)
            decrypt = raw_input("decript yes or no:")
            if decrypt == "yes":
                vg_1.decipher(cipher_text,key)
                decrypt_text = vg_1.decipher(cipher_text,key)
                print("Decrypted finished!")
                print(decrypt_text)
                continue
        elif type =='des':
            des_1 = des()
            key_file = raw_input("Please input the path of key file:")
            string_file = raw_input("Please input the path of the plain_text file:")
            des_1.encryption(key_file,string_file)
            options = raw_input('decrypt yes or no:')
            if options == "yes":
                des_file = raw_input("Please input the path of des file:")
                key_file = raw_input("Please input the path of key file:")
                des_1.decryption(key_file,des_file)
            else:
                continue
        elif type == 'md5':
            md5_1 = MD5_State()
            key = raw_input("key:")
            buff = [''] * 16
            ciper = md5_1.md5_digest(key, len(key), buff)
            print('Encypt success!')
            print("ciper_text =")
            for i in range(16):
                print("%x" % ((ord(buff[i]) & 0xF0) >> 4), end='')
                print("%x" % (ord(buff[i]) & 0x0F), end='')
            print('\n')
        elif type == 'rsa':
            rsa_1 = xRsa()
            string = raw_input("plaintext:")
            cipher = rsa_1.encrptyMsg(string)
            print("cipher text:" + str(cipher))
            options = raw_input('decrypt yes or no:')
            if options == "yes":
                plaintext = rsa_1.decrptyMsg(cipher)
                print("decrypted text:" + plaintext)
            else:
                continue
        else:
            continue





