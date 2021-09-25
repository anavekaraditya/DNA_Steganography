message = str(input("Enter your message : "))

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

amino_acids = [[['GCU','GCC','GCA','GCG'],['A']],[['CGA','CGG','AGA','AGG'],['R']],[['AAU','AAC'],['N']],
               [['GAU','GAC'],['D']],[['UGU','UGC'],['C']],[['CAA','CAG'],['Q']],[['GAA','GAG'],['E']],
               [['GGU','GGC','GGA','GGG'],['G']],[['CAU','CAC'],['H']],[['AUU','AUC','AUA'],['I']],
               [['UAA','UGA','UAG'],['B']],[['CGU','CGC'],['U']],[['GUC'],['Z']],[['UUA','UUG','CUU'],['L']],
               [['AAA','AAG'],['K']],[['AUG'],['M']],[['UUC','UUU'],['F']],[['CCU','CCC','CCA'],['P']],
               [['UCU','UCC','AGU','AGC'],['S']],[['ACU','ACC','ACA','ACG'],['T']],[['UGG'],['W']],
               [['UAU','UAC'],['Y']],[['GUU','GUA'],['V']],[['CUA','CUG'],['O']],[['UCA','UCG'],['X']],[['CUC','CCG','GUG'],['J']]]
