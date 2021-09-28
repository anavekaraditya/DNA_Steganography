message = str(input("Enter your message : "))


"""
amino_acids = [[['GCU','GCC','GCA','GCG'],['A']],[['CGA','CGG','AGA','AGG'],['R']],[['AAU','AAC'],['N']],
               [['GAU','GAC'],['D']],[['UGU','UGC'],['C']],[['CAA','CAG'],['Q']],[['GAA','GAG'],['E']],
               [['GGU','GGC','GGA','GGG'],['G']],[['CAU','CAC'],['H']],[['AUU','AUC','AUA'],['I']],
               [['UAA','UGA','UAG'],['B']],[['CGU','CGC'],['U']],[['GUC'],['Z']],[['UUA','UUG','CUU'],['L']],
               [['AAA','AAG'],['K']],[['AUG'],['M']],[['UUC','UUU'],['F']],[['CCU','CCC','CCA'],['P']],
               [['UCU','UCC','AGU','AGC'],['S']],[['ACU','ACC','ACA','ACG'],['T']],[['UGG'],['W']],
               [['UAU','UAC'],['Y']],[['GUU','GUA'],['V']],[['CUA','CUG'],['O']],[['UCA','UCG'],['X']],[['CUC','CCG','GUG'],['J']]]
"""

amino_acids1 = {'GCU':'A','CGA':'R','AAU':'N','GAU':'D','UGU':'C',
                'CAA':'Q','GAA':'E','GGU':'G','CAU':'H','AUU':'I',
                'UAA':'B','CGU':'U','GUC':'Z','UUA':'L','AAA':'K',
                'AUG':'M','UUC':'F','CCU':'P','UCU':'S','ACU':'T',
                'UGG':'W','UAU':'Y','GUU':'V','CUA':'O','UCA':'X',
                'CUC':'J'}

amino_acids2 = {'GCC':'A','CGG':'R','AAC':'N','GAC':'D','UGC':'C',
                'CAG':'Q','GAG':'E','GGC':'G','CAC':'H','AUC':'I',
                'UGA':'B','CGC':'U','UUG':'L','AAG':'K','UUU':'F',
                'CCC':'P','UCC':'S','ACC':'T','UAC':'Y','GUA':'V',
                'CUG':'O','UCG':'X','CCG':'J'}

amino_acids3 = {'GCA':'A','AGA':'R','GGA':'G','AUA':'I','UAG':'B',
                'CUU':'L','CCA':'P','AGU':'S','ACA':'T','GUG':'J'}

amino_acids4 = {'GCG':'A','AGG':'R','GGG':'G','AGC':'S','ACG':'T',}


def m_to_mbin(message):
    mbin = ''
    for i in message:
        m_ascii = ord(i)
        m_ascii_bin = bin(m_ascii)[0] + bin(m_ascii)[2:]
        mbin += str(m_ascii_bin)
    return mbin

mbin = m_to_mbin(message)
print(mbin)

def mbin_to_mdna(mbin):
    mdna=''
    for i in range(0, len(mbin), 2):
        j = mbin[i:i+2]
        if j == "00" :
            mdna += 'A'
        elif j == "01":
            mdna += 'C'
        elif j == "10":
            mdna += 'G'
        elif j == "11":
            mdna += 'T'
    return mdna
    
mdna = mbin_to_mdna(mbin)
mdna = mdna.replace('T','U')
print(mdna)
ex=len(mdna)%3
print(ex)
if ex!=0:
    mdna+='A'*(3-ex)
print(mdna)

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

print(maa)
m1dna = mbin_to_mdna(m_to_mbin(maa)) 
print(m1dna)
print(amb)    


