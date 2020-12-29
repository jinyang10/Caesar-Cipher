# Jin Yang 260724904

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# takes a str input, returns True if input is non-empty str containing only characters from the English alphabet,
# False otherwise. Should NOT be case sensitive.

def in_engl_alpha(eng):
    """ (str) -> bool
    Returns true if str input is non-empty and contains only characters from the English alphabet,
    returns false otherwise. Function is not case sensitive.
    
    >>> in_eng_alpha('a')
    True
    >>> in_eng_alpha('BaT')
    True
    >>> in_eng_alpha('@')
    False
    >>> in_eng_alpha('you and I)
    False
    """
    if eng.lower() in [" ",""]:
        return False
    
    for i in range(len(eng.lower())):
        if eng.lower()[i] not in ALPHABET:
            return False
    
    return True

# takes a single character str and an int 'n' as input. ValueError if str is not one character. Otherwise, if
# the character is a letter of the alphabet, Returns the lower case letter which appears 'n' position later
# in the alphabet. If the character is not a letter of alphabet, Returns the character unmodified. 
def shift_char(single, n):
    """ (str, int) -> str
    Takes a single character str and an int n as input. Raises ValueError is str is not one character.
    Otherwise, returns the lower case letter which appears n positions later in the alphabet. If the
    character isn't a letter of the alphabet, returns the character umodified.
    
    >>> shift_char('a', 5)
    'f'
    >>> shift_char('Z', 3)
    'c'
    >>> shift_char('$', 10)
    '$'
    >>> shift_char('haha', 4)
    Traceback (most recent call last):
    ValueError: the string should have only one character
    >>> shift_char('o', 86)
    'w' 
    """
    if len(single) != 1:
        raise ValueError("the string should have only one character")
    
    if in_engl_alpha(single) == False:
        return single
        
    for i in range(len(ALPHABET)):
        if single.lower() == ALPHABET[i]:
            break 
    
    return ALPHABET[(i + n) % 26] 

# same as shift_char(single, n), except takes as input a str of 1 or more characters. 
def shift_chars(multi, n):
    """ (str) -> int
    Takes as input a str and an int. Returns a lower case string consisting of each character of the
    input string shifted n times in the alphabet. If the input string is not in alphabet, return a space string.
    If the input string is the empty string, return the empty string. If the input string contains space,
    return a space string.
    
    >>> shift_chars('c@t', 3)
    'f w'
    >>> shift_chars('', 3)
    ''
    >>> shift_chars('you and I', -2)
    'wms ylb g'
    """
    multi = multi.lower()
    multi_str = ""
    
    for i in range(len(multi)):
        if multi[i] in [' '] or multi[i] not in ALPHABET:
            multi_str = multi_str + ' '
        
        if multi[i] in ALPHABET:
            multi_str = multi_str + ALPHABET[(ALPHABET.index(multi[i]) + n) % 26]
        
            
    return multi_str   
         
# takes str as input, Returns list of int. Elements of list correspond to the position (counting from 0) of
# each character in the string, as a letter of the English alphabet. If the string received as input is a
# non-empty string containing characters other than letters from the English alphabet, raise ValueError.

def get_keys(key):
    """ (str) -> [list]
    Takes a str as input, returns a list of int. The elements of list correspond to the position
    (counting from 0) of each character in the str as a letter of the English alphabet. If the str received as
    input is a non-empty str containing characters other than letters from the English alphabet, raise
    ValueError.
    
    >>> get_keys('he$lo')
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    >>> get_keys('abC')
    [0, 1, 2]
    >>> get_keys('hi there')
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    """
    key = key.lower()
    
    for i in range(len(key)):
        if key[i] not in ALPHABET:
            raise ValueError("the input string must contain only characters from the English alphabet")
    
    # iterate through the indexes of key, compare each index of key to each index of ALPHABET,
    # if key[index] == ALPHABET[index], Return position of ALPHABET[index]
    
    alpha_list = []
    for i in range(len(key)):
        if key[i] in ALPHABET:
            alpha_list.append(ALPHABET.find(key[i]))
        
    return alpha_list

# take a str and an int 'n' as input. Returns a string of length n, obtained by concatenating characters of the
# input string together, until the desired length is matched. Note: n can be smaller than the length of the
# input string. If the input string is empty, raise ValueError.

def pad_keyword(word, n):
    """ (str, int) -> str
    Returns a string of length n, obtained by concatenating characters of the input string together, until
    the desired length is matched. Note: n can be smaller than the length of the input string. If the
    input string is empty, raise ValueError. If n is less than 0, return ValueError (n must be greater than
    0).
    
    >>> pad_keyword('hi there', 5)
    'hi th'
    >>> pad_keyword('', 5)
    Traceback (most recent call last):
    ValueError: the input string should not be empty
    >>> pad_keyword('yeet', -2)
    Traceback (most recent call last):
    ValueError: the input integer should be greater than 0
    """
    if word in [""]:
        raise ValueError("the input string should not be empty")
    
    if n < 0:
        raise ValueError("the input integer should be greater than 0")
    
    # iterate through word[index], return each word[index] n times.
    word_str = ""
    
    if n < len(word):
        for i in range(n):
            word_str = word_str + word[i]
    
        return word_str
    
    if n >= len(word):
        word_str = word_str + word * (n // len(word))
        
        for i in range(n % len(word)):
            word_str = word_str + word[i]
            
            
        return word_str
     

            
            
        
        
    
    
            
    
    
        

        
    
