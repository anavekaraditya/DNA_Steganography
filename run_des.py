import pyDes
import main

# i = input("Enter any string: ")

# Padding function: add ' ' until the string length is multiples of 8
def padded_text(s):
    while len(s) % 8 != 0:
        s += ' '
    return s


# key should be 8 bytes long.
# k_ecb = pyDes.des("DESCRYPT", pyDes.ECB)
#
## encrypted data i.e. in bytes
# e_ecb = k_ecb.encrypt(p)
# print("\n The encrypted string(in bytes) - \n", e_ecb)
# string = e_ecb.decode('utf-16')
# print(string)
# str_byte = string.encode('utf-16')[2:]
# print(str_byte)
##print(bytes.fromhex(string))
## extract the input text from the encrypted input using decryption'
# d_ecb2 = k_ecb.decrypt(str_byte)
# d_ecb = k_ecb.decrypt(e_ecb)
# print("\n The actual input(in bytes) -  \n", d_ecb.decode('utf-8'))
# print("\n The actual input(in bytes) -  \n", d_ecb2.decode('utf-8'))
#

def enc_des(text, key):
    text = padded_text(text)
    key = key[:8]
    k_ecb = pyDes.des(key, pyDes.ECB)
    e_ecb = k_ecb.encrypt(text)
    print(e_ecb)
    #encrypted = e_ecb.decode('utf-16')
    encrypted = e_ecb.hex()
    print(encrypted)
    return encrypted


def dec_des(text, key):
    key = key[:8]
    k_ecb = pyDes.des(key, pyDes.ECB)
    #e_ecb = text.encode('utf-16')[2:]
    e_ecb = bytes.fromhex(text)
    d_ecb = k_ecb.decrypt(e_ecb)
    decrypted = d_ecb.decode('utf-8')
    print(decrypted)
    return decrypted


#e = enc_des('awdadawfecvwditya', 'asdfqwer')
#eb = main.m_to_mbin(e)
#print(eb)
#ea = main.mbin_to_m(eb)
#print(ea)
#dec_des(e, 'asdfqwer')
