from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA

class myDES():
	def __init__(self, keytext,ivtext):
		hash = SHA.new()
		hash.update(keytext.encode())
		key = hash.digest()
		self.key = key[:24]
		
		hash.update(ivtext.encode())
		iv = hash.digest()
		self.iv = iv[:8]

	def enc(self,plaintext):
		des3 = DES3.new(self.key,DES3.MODE_CFB,self.iv)
		encmsg = des3.encrypt(plaintext.encode())
		return encmsg
	
	def dec(self,ciphertext):
		des3 = DES3.new(self.key,DES3.MODE_CFB,self.iv)
		decmsg = des3.decrypt(ciphertext)
		return decmsg
	
def main():
	keytext = 'samsjang'
	ivtext = '1234'
	msg = 'python35'

	myCipher = myDES(keytext,ivtext)
	ciphered = myCipher.enc(msg)
	deciphered = myCipher.dec(ciphered)
	print('ORIGINAL:\t%s'%msg)		
	print('CIPHERED:\t%s'%ciphered)
	print('DECIPHERED:\t%s'%deciphered)
	print(deciphered.decode('utf-8'))

def enc_des3(text,key):
	ivtext = 'Crypteg'
	myCipher = myDES(key, ivtext)
	ciphered = myCipher.enc(text).hex()
	print(ciphered)
	return ciphered

def dec_des3(text,key):
	ivtext = 'Crypteg'
	myCipher = myDES(key, ivtext)
	text = bytes.fromhex(text)
	deciphered = myCipher.dec(text).decode('utf-8')
	print(deciphered)
	return deciphered

#e = enc_des3('Adityddfgfgdfa','DESCPYTE')
#dec_des3(e,'DESCPYTE')


		
