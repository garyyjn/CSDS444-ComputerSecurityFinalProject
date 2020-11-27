import string
class VG:
    def __init__(self):
        self.characters_26= "abcdefghijklmnopqrstuvwxyz"
        self.dict_key = {}
        self.dict_char2int = {}
        self.dict_int2char = {}
        self.table = []

    def create_table(self,key):
        length_key = len(key)
        i = 0
        while i < length_key:
            self.table.append({})
            i = i + 1
        #print self.table
        length_characters = len(self.characters_26)
        for index in range(0,length_key):
            self.dict_key.update({key[index]:index})
            print(self.dict_key)
        for index in range(0,length_characters):
            self.dict_char2int.update({self.characters_26[index]:index})
        for index in range(0,length_characters):
            self.dict_int2char.update({index:self.characters_26[index]})
        for key in self.dict_key.keys():
            temp_int_key = self.dict_char2int.get(key)
            for key_1 in self.dict_char2int.keys():
                temp_int_char = self.dict_char2int.get(key_1)
                cipher_int = divmod(temp_int_key + temp_int_char,26)[1]-1
                if cipher_int == -1:
                    cipher_int = 25
                cipher_char = self.dict_int2char.get(cipher_int)
                self.table[self.dict_key.get(key)].update({temp_int_char:cipher_char})
        j = 0
        while j < length_key:
            #print self.table[j]
            j = j+1
        return self.table

    def cipher(self,plaintext,key):
        length_plaintext = len(plaintext)
        length_key = len(key)
        new_string = ''
        index = 0
        while index < length_plaintext:
            char = plaintext[index]
            colum = self.dict_char2int.get(char)
            #print self.dict_char2int
            row = divmod(index,length_key)[1]
            dict = self.table[row]
            cipher_char = dict.get(colum)
            new_string = new_string + cipher_char
            index = index + 1
        return new_string

    def decipher(self,cipher_text, key):
        length_key = len(key)
        length_cipger = len(cipher_text)
        index = 0
        index_1 = 0
        new_string = ''
        while index < length_cipger:
            row = divmod(index,length_key)[1]
            while index_1 < 26:
                dict = self.table[row]
                if dict.get(index_1) == cipher_text[index]:
                    plain_char = self.dict_int2char.get(index_1)
                    new_string = new_string + plain_char
                    index_1 = 0
                    break
                else:
                    index_1 = index_1 + 1
                    continue
            index = index + 1
        return  new_string

# Description how to use it
'''
key = input('key:')
input_string = raw_input('input_string:')
obj = VG()
obj.create_table(key)
print('key')
print(obj.dict_key)
print(obj.dict_char2int)
print(obj.dict_int2char)
print(obj.table)

ciper_text = obj.cipher(input_string,key)
print(ciper_text)
deciper_text = obj.decipher(ciper_text,key)
print(deciper_text)
'''