# DNA_Steganography
 DWS Project

# Abstract
Although cryptography and steganography can be used to provide data security, each has its 
own problem. The problem with Cryptography is that, the cipher text looks ridiculous, so the 
attacker will interrupt the transfer or carefully examine the data from the sender to the receiver. 
The problem with Steganography is that when the existence of hidden information is revealed 
or even suspected, the message is known. In this paper, an integrated data protection strategy 
is proposed using Cryptography and Steganography techniques to improve information 
security. First, the DNA transcription method in Cryptography and the LSB Steganography 
method are proposed. In this proposed model the input is taken in the form of text and can be 
hidden in pictures and can be retrieved from the image to the text.

# Proposed Method (or) System Design
This section gives a brief description of the overall process used in the proposed model and 
how each module works. We will discuss about DNA encoding technique in Cryptography and 
LSB steganography method. It also includes a module called the algorithm selector. The overall 
flow of the method is shown in the Figure.

So, the proposed model comprises of a total of 3 modules and are used in the order given below 
in Figure 1. The input is taken in text form (characters). i.e., text data can be hidden into images 
and can be retrieved back as text. 


# DNA Cryptography
DNA Encoding:
The input data (secret data) is pre-processed before it is encoded. First the text is converted 
into 8-bit binary form using its ASCII value. These binary bits are then coded into nitrogen 
bases (A, T, G, C). this encoding is done using the 2-bit conversion which is explained in the 
below table. 

The nitrogen bases are split into codon of 3 of 3 bases. These codons are converted to RNA by 
replacing ‘T’ with ‘U’ and are then converted into its corresponding amino acids using this 
amino acid table. During the conversion of RNA to Amino acids ambiguity bits are separately 
recorded and stored. The need of ambiguity is due the factor that there are many amino acids 
with more than one RNA mapped to it. For each RNA 2-bit ambiguity is noted. For example, 
‘10’ is recorded if the 3rd mapped RNA is matched. 

The amino acids are then converted back into binary form through 8-binary conversion. The 
resultant binary data is further sent as the encrypting message to be encrypt. 

# Encryption:
With the key and the algorithm selector the encryption algorithm is decided and the message 
is encrypted by the key. In this paper we have included 4 encryption algorithms. The algorithms 
are AES, DES, 3DES, IDEA. 
AES and IDEA encryption uses 128 bits key and follows the standard procedure. DES 
encryption uses 64 bits key and follows the ECB mode of encryption. 3DES encryption uses 
168 bits key and follows the CFB mode of encryption. With variable key lengths the key length 
in modified based on the algorithm selected.
The selected algorithm encrypts the message and outputs in binary form. This binary data is 
then sent to the LSB embedding module.
DNA Encryption steps:
1. Convert the Secret data (message M) into its 8-bit binary form from its ASCII values.
2. Using the 2-bit binary to DNA coding convert the binary into DNA bases.
3. Replace the ‘T’ with ‘U’ in the nitrogen bases to make it into RNA form.
4. Split the RNA data into codons (where each codon contains 3 DNA bases). And these 
codons are converted into the corresponding amino acid using the amino acid conversion 
table. Record the ambiguity bit during the conversion. 
5. The amino acid and ambiguity are appended as the DNA encoded message.
6. Key is processed in the algorithm selector and the encryption algorithm is selected. The 
key is further used to encrypt the DNA encoded message.
7. The encrypted message is taken in the form of binary which is sent to the embedding 
process to embed it onto the cover image.
The entire process of encryption is graphically represented in the figure below.


DNA Decoding:
The decoding process is completely reverse of all the operation done in the encoding part. First 
the data retrieved from the image is decrypted using the corresponding encryption algorithm 
which is obtained from the key provided. The decrypted data is in binary and the same steps 
involved in the encryption is followed in the reverse order. 

DNA Decryption steps:

1. Retrieve the embedded bits (Cipher text) from the stego image.
2. Select the decrypting algorithm using the key and algorithm selector.
3. Decrypt the cipher text using the algorithm and obtain the binary form of it.
4. Convert the binary to characters using the 8-bit binary ASCII value conversion. This 
conversion gives us the corresponding amino acids.
5. Map the amino acid with its respective RNA codons (3 DNA bases). This is done using 
the Ambiguity bits retrieved from the image. The mapped DNA codons are recorded. 
6. The DNA is converted back to its binary form using the 2-bit DNA-Binary coding. 
7. Finally, the binary data is converted into text using the 8-bit ASCII value conversion.
8. The resultant text is the secret message stored by the sender. These steps will only work 
only if the key value provided is exactly same as the key provided by the sender at the 
time of embedding.
The entire process of decryption is graphically represented in the figure below.

# Algorithm Selection 
The algorithm selector is used to decided which encryption algorithm is going to be 
implemented. The whole process only depends on the key as the key is kept confidential. This 
makes the encryption more secure as the probability of decrypting the message without the key 
reduces and increases the time for brute forcing. 
First the key in converted into binary from its ASCII value. Then the decimal value of the 
whole binary value is taken. This decimal value is then put into this formula of Modula 4 and 
the resultant is used to decide which algorithm to be used.
Q = decimal value MOD 4
Q = 0,1,2,3
As in this paper we have include 4 algorithms, each algorithm is given an index number 
(0,1,2,3). The ‘Q’ is matched with the index number and the algorithm is selected. 
For the attacker to decrypt it without the key would have to brute force it by checking all the 
algorithms as it is not certain to be encrypted with a single algorithm.

# LSB Steganography
LSB steganography technique is one of most common methods of embedding information into 
the cover image. This method stores data in the least significant bits by replacing LSB bits of 
the pixel values with the data bits. The LSB bits are selected based on the size of the data to be 
embedded. 
In the proposed model, we deal with RGB channels of the image and embed in all 3 channels. 
The model which finally receives the embedding bits from the above modules calculates the 
size and estimates the LSB bits. This process involves the information of the cover image which 
helps to calculate the available pixels on which embedding can be done. The embedding bits 
are replaced in the LSB bits of all 3 channels. The embedding data contains 2 different parts of 
information. The first one is the encrypted bits and the ambiguity bits and the second contains 
the length of the total data embedded and the length of ambiguity bits. The second part is 
embedded on fixed pixels. That is the last 32 pixels of the image. Except these 32 pixels the 
remaining pixels are available for embedded. 
For short message which have a smaller number of embedding data then the total number of 
bits in the image the model finds the interval value by which the pixels are skipped. This helps 
to spread the embedding throughout the image and not only in the initial part of the image in 
the case of short messages.
