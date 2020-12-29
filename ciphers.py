# Jin Yang 260724904

import crypto_helpers as crypto

# takes as input a str (message to encrypt/decrypt), an int k (the key of the cipher), an int m representing
# the mode (encrypt/decrypt). If m = 1, mode encrypt; if m = -1, mode decrypt. If m is anything else, ValueError
# indicating no other mode available. RETURNS a string obtained by encrypting or decrypting (depending on m) the
# message received as input, using the Caesar's cipher with key k.

def caesar(message, key, mode):
    """ (str, int, int) -> str
    Takes as input a str message, int key, and int mode. If mode = 1, call on crypto.shift_chars to encrypt.
    If mode = -1, call on crypto.shift_chars with -key to decrypt. If mode is anything else,
    raise ValueError indicating no other mode available. Returns the resulting string.
    
    >>> caesar('wtAAd', 15, -1)
    'hello'
    >>> caesar('hi there', 10, 1)
    'rs drobo'
    >>> caesar('hi', 10, 5)
    Traceback (most recent call last):
    ValueError: mode not supported
    >>> caesar('HI', 0, 1)
    'hi'
    """
    if mode not in [1, -1]:
        raise ValueError("mode not supported")
    
    if mode == 1:
        return crypto.shift_chars(message, key)
    
    if mode == -1:
        return crypto.shift_chars(message, -key)

# takes as input a str (message to encrypt/decrypt), another str (key of the cipher), and an int m
# (mode: encrypt or decrypt). m = 1 is encrypt, m = -1 is decrypt, any other value raises ValueError
# indicating no other mode's supported. RETURNS a string obtained by encrypting or decrypting (depending on m)
# the message received as input (using Vigenere's cipher with key received as input). Raise ValueError if
# string representing key is empty.

def vigenere(message, key, mode):
    """ (str, str, int) -> str
    Takes as input a str message, str key, and int mode. If mode = 1, call crypto.pad_keyword, crypto.get_keys,
    and crypto.shift_char to encrypt message. If mode = -1, call the same functions to decrypt message. Returns
    the resulting string. Raise ValueError if the string key is empty.
    
    >>> vigenere('baNAna', 'apple', 1)
    'bpclra'
    >>> vigenere('hi there', 'you', 1)
    'fw rvyps'
    >>> vigenere('fw rvyps', 'you', -1)
    'hi there'
    >>> vigenere('hi', '', 1)
    Tracback (most recent call last):
    ValueError: the input string should not be empty
    >>> vigenere('hi there', 'you', 5)
    Tracback (most recent call last):
    ValueError: mode not supported
    """
    if mode not in [1, -1]:
        raise ValueError("mode not supported")
    
    if mode == 1:
        # get len(message) characters of key
        updated_key = crypto.pad_keyword(key, len(message))
        
        # Get the position of each index of updated_key corresponding to the alphabet
        pos_updated_key = crypto.get_keys(updated_key)
        
        # take each value at pos_updated_key[index], move each character of 'message' at each
        # pos_updated_key[index], pos_updated_key[index] times.
        final_string = ''
        for i in range(len(pos_updated_key)):
            final_string += crypto.shift_char(message[i], pos_updated_key[i])
              
        return final_string
    
    if mode == -1:
        # get len(message) characters of key
        updated_key = crypto.pad_keyword(key, len(message))
        
        # Get the position of each index of updated_key corresponding to the alphabet
        pos_updated_key = crypto.get_keys(updated_key)
        
        # take each value at pos_updated_key[index], move each character of 'message' at each
        # pos_updated_key[index], pos_updated_key[index] times.
        final_string = ''
        
        for i in range(len(pos_updated_key)):
            final_string += crypto.shift_char(message[i], -pos_updated_key[i])
            
        return final_string   
        
        
        
    
    
        
        
    
    