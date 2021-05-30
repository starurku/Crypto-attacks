from roots import *
from Crypto.Hash import SHA
import sys
def attacker(mesage) :

	sha_digest = SHA.new(message).hexdigest()
	prefix = "0001" 
	padding_bytes = "ff"*abs((256/8-38)) 
	suffix = "00" + "3021300906052B0E03021A05000414" + sha_digest + "1234"*106 #garbage value
	result = prefix + padding_bytes + suffix #padding 6 bytes of "ff" and garbage values to ensure message is equal to RSA keysize (256 bytes)
	cube_root = integer_nthroot(int(result,16) , 3) #cube root over the integers
        print integer_to_base64(cube_root[0]) #the signature seems to work with and without rounding up.

if __name__ == "__main__": 
    message = sys.argv[1]
    attacker(message)
