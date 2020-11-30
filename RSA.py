# -*- coding: utf-8 -*-
import random
import binascii
from pip._vendor.distlib.compat import raw_input
class xRsa(object):	
	n = 0
	e = 0
	d = 0
	msgLen = 100 # the len of string
	"""
	RSA theory
	The RSA algorithm involves three parameters, n, e, d.
	Among them, n is the product of two large prime numbers p and q, and the number of bits occupied by the binary representation of n is the so-called key length.
	e1 and d are a pair of related values, e can be taken arbitrarily, but e and (p-1)*(q-1) are required to be relatively prime; then choose d, requiring (d*e1)mod((p-1) *(q-1))=1.
	(N, e), (n, d) is the key pair. Among them, (n, e) is the public key, and (n, d) is the private key. [1] 
	The algorithms of RSA encryption and decryption are exactly the same. Set A as plaintext and B as ciphertext, then: A=B^d mod n; B=A^e mod n; (In the public key encryption system, public key encryption is generally used, private Key decryption)
	e and d can be used interchangeably, namely:
	A=B^d mod n; B=A^e mod n;
	"""

	"""
	The constructor generates key data such as public keys and private keys
	"""
	def __init__(self):
		print ("This is the class xRsa! According to RSA theory, use Python to realize the encryption and decryption of this algorithm")
		p = self.find_prime_range(self.msgLen // 2)
		q = self.find_prime_range(self.msgLen // 2)
		print ("Find RSA prime p:" + str(p))
		print ("Find RSA prime q:" + str(q))
		#Calculate the product n = p * q, calculate phi(n) = (p-1)*(q-1), where phi(n) is the Euler function of n
		self.n  = p * q
		print ("Find RSA prime n:" + str(self.n))
		phi = (p -1) * (q -1)	
		#Here is a simple process to set a fixed value	
		self.e = 65537 
		print ("Find RSA prime e:65537")
		#Use the extended Euclidean algorithm to calculate the private key d. Satisfies d * e=1 (mod phi(n)), e and n are public keys, and d is a secret key.
		self.d = self.calc_for_d(phi, self.e)	
		print ("Find RSA prime d:" + str(self.d))   

	def calc_value_mode(self, b, n, m):
	    a1 = 1
	    a2 = b
        
	    while n:
	        if n & 0x1:
	            a1 = a1 * a2 % m
	        a2 = a2 * a2 % m
	        n >>= 1
	    return a1		
	
	def is_prime_value(self, n):
	        q = n - 1
	        k = 0
	       
	        while q % 2 == 0:
	            k += 1
	            q = q // 2
	        a = random.randint(2, n - 2)
	        
	        if self.calc_value_mode(a, q, n) == 1:
	            return True
	        
	        for j in range(0, k):
	            if self.calc_value_mode(a, (2 ** j) * q, n) == n - 1:
	                return True	       
	        return False		

	def recursive_computation(self, a, b):
	    if b == 0:
	        return 1, 0, a
	    else:
	        x, y, q = self.recursive_computation(b, a % b)
	        #x = y
	        #y = (x - (a // b) * y)
	        x, y = y, (x - (a // b) * y)
	        return x, y, q

	def calc_for_d(self, phi, e):
	    (x, y, r) = self.recursive_computation(phi, e)	   

	    if y < 0:	        
	        return y + phi  
	    return y

	#find p q
	def find_prime_range(self, xlen):
	    while True:
	        n = random.randint(0, 1 << xlen)
	        if n % 2 != 0:
	            found = True	            
	            for i in range(0, 5):   
	                if self.is_prime_value(n) == False:
	                    found = False
	                    break
	            if found == True:
	                return n

	def ToLong(self, msg):		
	    string3 = msg.encode('utf-8')
	    #return int(msg.encode('hex'), 16)
	    return int(binascii.hexlify(string3),16)
	    #return msg.encode('utf8')

	def ToStringEx(self, long_num):
	    #str = hex(long_num)[2:].replace("L","") 
        
	    #if len(str) % 2 != 0: str = '0' + str
	    #return str.decode('hex')
	    return str(binascii.unhexlify(hex(long_num)[2:]))

       def encrptyMsg(self, msg):

       	    mess_num = self.ToLong(msg)
            tmpxx = "Ready to encrypt,public key:" + str(self.e) + "^" + str(self.n)
            print (tmpxx)
            cipher = self.calc_value_mode(mess_num, self.e, self.n)

            return cipher, self.d,self.n

      def decrptyMsg(self,msg,d,n):
            tmpxx = "Ready to decrpty,private key:" + str(self.d) + "^" + str(self.n)
            print (tmpxx)
            plaintext1 = self.calc_value_mode(msg, d, n)
            plaintext2 = self.ToStringEx(plaintext1)
            return plaintext2

if __name__ == '__main__':
    msg = raw_input('Message: ')
    #Create an object, change the internal of the object will complete the relevant initialization, especially the private key, public key
    t = xRsa()
    #Encrypt and return the result
    print ("plain text:" + msg)
    cipher = t.encrptyMsg(msg)
    print ("cipher text:" + str(cipher))
    #Decrypt and return the result
    plaintext = t.decrptyMsg(cipher)
    
    # Print the string content after encryption and decryption
    print ("decrypted text:"+plaintext)
    
