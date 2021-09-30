message = str(input("Enter your Message : "))
key = str(input("Enter the Key:"))

"""
amino_acids = [[['GCU','GCC','GCA','GCG'],['A']],[['CGA','CGG','AGA','AGG'],['R']],[['AAU','AAC'],['N']],
               [['GAU','GAC'],['D']],[['UGU','UGC'],['C']],[['CAA','CAG'],['Q']],[['GAA','GAG'],['E']],
               [['GGU','GGC','GGA','GGG'],['G']],[['CAU','CAC'],['H']],[['AUU','AUC','AUA'],['I']],
               [['UAA','UGA','UAG'],['B']],[['CGU','CGC'],['U']],[['GUC'],['Z']],[['UUA','UUG','CUU'],['L']],
               [['AAA','AAG'],['K']],[['AUG'],['M']],[['UUC','UUU'],['F']],[['CCU','CCC','CCA'],['P']],
               [['UCU','UCC','AGU','AGC'],['S']],[['ACU','ACC','ACA','ACG'],['T']],[['UGG'],['W']],
               [['UAU','UAC'],['Y']],[['GUU','GUA'],['V']],[['CUA','CUG'],['O']],[['UCA','UCG'],['X']],[['CUC','CCG','GUG'],['J']]]
"""

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
print(mbin)

def mbin_to_mdna(mbin):
    mdna=''
    for i in range(0, len(mbin), 2):
        j = mbin[i:i+2]
        mdna+=dna[j]
    return mdna
    
def mdna_to_mbin(mdna):
    mbin=''
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


print(mdna)
x = mdna_to_maa(mdna)
maa = x[0]
amb = x[1]
print(maa)
print(amb)   
m1dna = mbin_to_mdna(m_to_mbin(maa)) 
print(m1dna)
print(mbin_to_m(mbin))
mdna=mdna.replace('U','T')
print(mdna_to_mbin(mdna))
print(maa_to_mdna(maa,amb))