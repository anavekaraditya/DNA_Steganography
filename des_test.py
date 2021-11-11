import pyDes
i = input("Enter any string: ")

# Padding function: add ' ' until the string length is multiples of 8
def padded_text(s):
    while len(s)%8 !=0 :
        s += ' '
    return s

p = padded_text(i)

# key should be 8 bytes long.
k_ecb = pyDes.des("DESCRYPT", pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=None)

# encrypted data i.e. in bytes
e_ecb = k_ecb.encrypt(p)
print("\n The encrypted string(in bytes) - \n", e_ecb)
string = e_ecb.hex()
print(string)
print(bytes.fromhex(string).decode('utf-16'))
# extract the input text from the encrypted input using decryption
d_ecb = k_ecb.decrypt(e_ecb)
print("\n The actual input(in bytes) -  \n", d_ecb.decode('utf-8'))