import string

characters_26= "abcdefghijklmnopqrstuvwxyz"
#key = "abcdefg"
#input_string = 'johnnydai'
dict_key = {}
dict_char2int = {}
dict_int2char = {}
table = []

def create_table(key,characters):
    length_key = len(key)
    i = 0
    while i < length_key:
        table.append({})
        i = i + 1
    print table
    length_characters = len(characters)
    for index in range(0,length_key):
        dict_key.update({key[index]:index})
    for index in range(0,length_characters):
        dict_char2int.update({characters[index]:index})
    for index in range(0,length_characters):
        dict_int2char.update({index:characters[index]})
    for key in dict_key.keys():
        temp_int_key = dict_char2int.get(key)
        for key_1 in dict_char2int.keys():
            temp_int_char = dict_char2int.get(key_1)
            cipher_int = divmod(temp_int_key + temp_int_char,26)[1]-1
            if cipher_int == -1:
                cipher_int = 25
            cipher_char = dict_int2char.get(cipher_int)
            table[dict_key.get(key)].update({temp_int_char:cipher_char})
    j = 0
    while j < length_key:
        print table[j]
        j = j+1
    return table

def cipher(plaintext,key):
    length_plaintext = len(plaintext)
    length_key = len(key)
    new_string = ''
    index = 0
    while index < length_plaintext:
        char = plaintext[index]
        colum = dict_char2int.get(char)
        row = divmod(index,length_key)[1]
        dict = table[row]
        cipher_char = dict.get(colum)
        new_string = new_string + cipher_char
        index = index + 1
    return new_string

def decipher(cipher_text, key):
    length_key = len(key)
    length_cipger = len(cipher_text)
    index = 0
    index_1 = 0
    new_string = ''
    while index < length_cipger:
        row = divmod(index,length_key)[1]
        while index_1 < 26:
            dict = table[row]
            if dict.get(index_1) == cipher_text[index]:
                plain_char = dict_int2char.get(index_1)
                new_string = new_string + plain_char
                index_1 = 0
                break
            else:
                index_1 = index_1 + 1
                continue
        index = index + 1
    return  new_string

key = raw_input('key:')
input_string = raw_input('input_string:')

create_table(key, characters_26)
print 'plaintext:' + input_string
print 'key:' + key
cipher_text = cipher(input_string,key)
print 'ciphertext:' + cipher_text
plaintext = decipher(cipher_text,key)
print 'plaintext:' + plaintext