from numpy import angle
import run_aes
import run_des
import time
from PIL import Image
import cv2

img = cv2.imread('Database/2.jpg')
img = cv2.resize(img,(500,500))
message = str(input("Enter your Message : "))
t1=time.time()
key = '1234567890123456'

dna = {'00':'A','01':'C','10':'G','11':'T'}
idna = {'A':'00','C':'01','G':'10','T':'11'}

amino_acids1 = {'GCU':'A','CGA':'R','AAU':'N','GAU':'D','UGU':'C',
                'CAA':'Q','GAA':'E','GGU':'G','CAU':'H','AUU':'I',
                'UAA':'B','CGU':'U','GUC':'Z','UUA':'L','AAA':'K',
                'AUG':'M','UUC':'F','CCU':'P','UCU':'S','ACU':'T',
                'UGG':'W','UAU':'Y','GUU':'V','CUA':'O','UCA':'X',
                'CUC':'J'}

iamino_acids1 = {v: k for k, v in amino_acids1.items()}

amino_acids2 = {'GCC':'A','CGG':'R','AAC':'N','GAC':'D','UGC':'C',
                'CAG':'Q','GAG':'E','GGC':'G','CAC':'H','AUC':'I',
                'UGA':'B','CGC':'U','UUG':'L','AAG':'K','UUU':'F',
                'CCC':'P','UCC':'S','ACC':'T','UAC':'Y','GUA':'V',
                'CUG':'O','UCG':'X','CCG':'J'}

iamino_acids2 = {v: k for k, v in amino_acids2.items()}

amino_acids3 = {'GCA':'A','AGA':'R','GGA':'G','AUA':'I','UAG':'B',
                'CUU':'L','CCA':'P','AGU':'S','ACA':'T','GUG':'J'}

iamino_acids3 = {v: k for k, v in amino_acids3.items()}

amino_acids4 = {'GCG':'A','AGG':'R','GGG':'G','AGC':'S','ACG':'T',}

iamino_acids4 = {v: k for k, v in amino_acids4.items()}

def m_to_mbin(message):
    mbin = ''
    for i in message:
        m_ascii = ord(i)
        m_ascii_bin = bin(m_ascii)[0] + bin(m_ascii)[2:]
        mbin += str(m_ascii_bin)
    return mbin

def mbin_to_m(message):
    m=''
    for i in range(0,len(message),8):
        t = message[i:i+8]
        m+=chr(int(t,2))
    return m

mbin = m_to_mbin(message)
print("mbin:", mbin)

def mbin_to_mdna(mbin):
    mdna=''
    w = len(mbin)%4
    mbin = mbin + ("0" * (4-w))
    for i in range(0, len(mbin), 2):
        j = mbin[i:i+2]
        mdna+=dna[j]
    return mdna
    
def mdna_to_mbin(mdna):
    mbin=''
    mdna=mdna.replace(' ','')
    for i in mdna:
        mbin+=idna[i]
    return mbin

mdna = mbin_to_mdna(mbin)
mdna = mdna.replace('T','U')
ex=len(mdna)%3
if ex!=0:
    mdna+='A'*(3-ex)

def mdna_to_maa(mdna):
    amb=''
    maa=''
    for i in range(0,len(mdna),3):
        j=mdna[i:i+3]
        if j in amino_acids1:
            amb+='00'
            maa+=amino_acids1[j]
        elif mdna[i:i+3] in amino_acids2:
            amb+='01'
            maa+=amino_acids2[j]
        elif mdna[i:i+3] in amino_acids3:
            amb+='10'
            maa+=amino_acids3[j]
        elif mdna[i:i+3] in amino_acids4:
            amb+='11'
            maa+=amino_acids4[j]
    return maa,amb

def maa_to_mdna(maa,amb):
    mdna=''
    n=0
    for i in range(0,len(amb),2):
        j = amb[i:i+2]
        if j == '00':
            mdna+=iamino_acids1[maa[n]]
        elif j == '01':
            mdna+=iamino_acids2[maa[n]]
        elif j == '10':
            mdna+=iamino_acids3[maa[n]]
        elif j == '11':
            mdna+=iamino_acids4[maa[n]]   
        n+=1     
    return mdna

print("mdna:",mdna)
x = mdna_to_maa(mdna)
maa = x[0]
amb = x[1]
print("maa:",maa)
print("amb:",amb)   
m1dna = mbin_to_mdna(m_to_mbin(maa)) 
print("m1dna:",m1dna)

q = int("".join(str(i) for i in m_to_mbin(key)),2)%2
print(q)
if q==1:
    cipherM = run_aes.enc_aes(m1dna,key)
elif q==0:
    cipherM = run_des.enc_des(m1dna,key)
print("cipherm before bin: ", cipherM)
cipherBin = m_to_mbin(cipherM)
print(cipherBin)
embData = cipherBin+amb

lamb = bin(len(amb))[0] + bin(len(amb))[2:]
print("lamb:",lamb)
lcb = bin(len(embData))[0] + bin(len(embData))[2:]
e = (500*500)//(3*len(embData))
print("lcb:",lcb)
lcbs = (48-len(lcb))*'0' + lcb
lambs = (48-len(lamb))*'0' + lamb

embData2 = lambs + lcbs
print("embdata1:",embData)
print("embdata2:",embData2)
i=0
for j in range(0,500):
    for k in range(0,500,e):
        for l in range(3):
            if i<len(embData):
                img[j,k,l] = int("".join(str(x) for x in bin(img[j,k,l])[0] + bin(img[j,k,l])[2:-1] + embData[i]),2)
                i+=1
            else:
                break
        

o=0
for j in range(467,500):
    for l in range(3):
        if o<len(embData2):
            img[499,j,l] = int("".join(str(x) for x in bin(img[499,j,l])[0] + bin(img[499,j,l])[2:-1] + embData2[o]),2)
            o+=1
        else:
            break
    

t3= time.time()
cv2.imshow("hello",img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() 
recData=""
recData2=""

for j in range(467,499):
    for o in range(3):
        recData2 = recData2 + bin(img[499,j,o])[-1]

print("recData2:", recData2)
LAMB = int("".join(str(i) for i in recData2[0:48]),2)
LCB = int("".join(str(i) for i in recData2[48:]),2)

print("Len of amb:",LAMB)
print("Len of recdata:",LCB)

i=0
for j in range(0,500):
    for k in range(0,500,e):
        for l in range(3):
            if i<LCB:
                recData = recData + bin(img[j,k,l])[-1]
                i+=1

print("recData:", recData)
LCBO = LCB-LAMB
print("Len of Cipher text only:",LCBO)
CIPHERm = recData[:LCBO]
AMB = recData[LCBO:]

print("Cipher text:",CIPHERm)
print("Amb:",AMB)

CIPHERm = mbin_to_m(CIPHERm)
print(CIPHERm)
if q==1:
    M1 = run_aes.dec_aes(CIPHERm,key)
elif q==0:
    M1 = run_des.dec_des(CIPHERm,key)

M1dna = M1
print("M1dna:", M1dna)
M1aa = mbin_to_m(mdna_to_mbin(M1dna))
print("M1aa:", M1aa)
Mdna = maa_to_mdna(M1aa,amb)
Mdna=Mdna.replace('U','T')
Mbin = mdna_to_mbin(Mdna)
M = mbin_to_m(Mbin)
print("Mdna:",Mdna)
print("Mbin:",Mbin)
print("M:",M)
t2=time.time()
print("Total time:", t3-t1)