message = str(input("Enter your message : "))

def m_to_mbin(message):
    mbin = ''
    for i in message:
        m_ascii = ord(i)
        m_ascii_bin = bin(m_ascii)[0] + bin(m_ascii)[2:]
        mbin = mbin + str(m_ascii_bin)
    return mbin

mbin = m_to_mbin(message)
print(mbin)

def mbin_to_mdna(mbin):
    mdna=''
    for i in range(0, len(mbin), 2):
        j = mbin[i:i+2]
        if j == "00" :
            mdna = mdna + 'A'
        elif j == "01":
            mdna = mdna + 'C'
        elif j == "10":
            mdna = mdna + 'G'
        elif j == "11":
            mdna = mdna + 'T'
    return mdna
    
mdna = mbin_to_mdna(mbin)
print(mdna)