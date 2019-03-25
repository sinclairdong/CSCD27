#!/usr/local/bin/python3
import binascii
import wave

#########################
####### RC4 #############
#########################

def ksa(key_b):
    ''' KSA - Key-scheduling algorithm (KSA)
    '''
    keylength = len(key_b)
    s = []
    for i in range(256):
        s.append(i)
    j = 0
    for i in range(256):
        j = (j + s[i] + key_b[i % keylength])%256
        (s[i], s[j]) = (s[j], s[i])

    return s

def prga(s):
    ''' PRGA - Pseudo-random generation algorithm
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]  # swap

        K = s[(s[i] + s[j]) % 256]
        yield K

def rc4(key_b,plaintext_b):
    ''' returns the RC4 ciphertext corresponding to the keys and plaintext given as bytes
    (bytes, bytes) -> bytes
    >>> rc4(b'Key',b'Plaintext')
    b'\xbb\xf3\x16\xe8\xd9@\xaf\n\xd3'
    '''
    S = ksa(key_b)
    keystream = prga(S)
    result = []
    for b in plaintext_b:
        result.append(bytes([(b ^ keystream.__next__())]))
    
    return b''.join(result)


#########################
####### utils ###########
#########################


def utf82bytes(s):
    ''' returns the bytes encoding of utf-8 string s given as argument
    (string) -> bytes
    >>> utf82ba('Key')
    b'Key'
    '''
    return s.encode('utf8')

def bytes2utf8(b):
    ''' returns the utf-8 string of the bytes ba given as parameter
    (bytes) -> string
    >>> ba2utf8(b'Key')
    'Key'
    '''
    return b.decode('utf8')

def armor2bytes(a):
    ''' returns the bytes of the ASCII armor string a given as parameter
    (string)-> bytes
    >>> armor2ba('S2V5')
    b'Key'
    '''
    return binascii.a2b_base64(a)

def bytes2armor(b):
    ''' returns the ASCII armor string of the bytes ba given as parameter
    (bytes)-> string
     >>> ba2armor(b'Key')
    'S2V5'
    '''
    return binascii.b2a_base64(b).decode('utf8')

#########################
### textfile support ####
#########################

def rc4_textfile_encrypt(key, input_filename, output_filename):
    ''' encrypts the input plaintext 
    file into the ASCI-armored output file using the key
    (string, string, string) -> None
    '''
    
    f_read = open(input_filename,'r')
    content = f_read.read()
    f_read.close()
    writing = bytes2armor(rc4(utf82bytes(key),utf82bytes(content)))
    f_write = open(output_filename, 'w+')
    f_write.write(writing)
    f_write.close()
    

def rc4_textfile_decrypt(key, input_filename, output_filename):
    ''' decrypts the ASCII-armored input file to the plaintext output file using the key
    (string, string, string) -> None
    '''
    
    f_read = open(input_filename,'r')
    content = f_read.read()
    f_read.close()
    content = bytes2utf8(rc4(utf82bytes(key),armor2bytes(content)))
    r_write = open(output_filename, 'w+')
    r_write.write(content)
    r_write.close()
    
#########################
### binary support ######
#########################

def rc4_binary(key, input_filename, output_filename):
    ''' encrypts/decrypts the binary input 
    file to the binary output file file using the key
    (string, string, string) -> None
    '''
    f_read = open(input_filename,'rb')
    content = f_read.read()
    content = rc4(utf82bytes(key),content)
    f_read.close()
    f_write = open(output_filename,'wb')
    f_write.write(content)
    f_write.close()
    
#########################
### wave support ########
#########################

def rc4_wave(key, input_filename, output_filename):
    ''' encrypts/decrypts the wave input 
    file to the wave output file file using the key
    (string, string, string) -> None
    '''
    f_read = wave.open(input_filename,'rb')
    (nchannels, sampwidth, framerate, nframes, comptype, compname
     )=f_read.getparams()
    content = rc4(utf82bytes(key),f_read.readframes(f_read.getnframes()))
    f_read.close()
    
    f_write = wave.open(output_filename,'wb')
    f_write.setparams(
        (nchannels, sampwidth, framerate, nframes, comptype, compname))
    f_write.writeframes(content)
    f_write.close()