'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_letter(letter, shift):
    if letter == " ":
        return letter
    shifted_letter = chr((ord(letter)) + shift)
    if shifted_letter > chr(90):
        new_shifted_letter =  chr((ord(letter)) + shift - 26)
        return new_shifted_letter
        print(new_shifted_letter)
    return shifted_letter
print("SHIFT LETTER")
letter = str(input('Enter letter here: '))
shift = int(input('Enter shift number here: '))
shifted_letter = shift_letter(letter, shift)
print(shifted_letter)


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def caesar_cipher(message, shift):  
    result = ""  
    result_caps = ""
    result_notcaps = "" 
    for i in range(len(message)):  
        char = message[i]   
        if (char.isupper()):
            result += chr((ord(char)) + shift)
            if result > chr(90):  
                result_caps += chr(((ord(char)) + shift - 26))
                return result_caps
                print(result_caps)
        else:  
            result += chr((ord(char)) + shift)
            if result > chr(122):  
                result_notcaps += chr(((ord(char)) + shift - 26))
                return result_notcaps
                print(result_notcaps)
    return result   
print('CAESAR CIPHER')
message = str(input("Enter message: "))  
shift = int(input('Enter shift number: '))
print("Cipher:",caesar_cipher(message,shift))  

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_letter(letter, letter_shift):
    if letter == chr(32):
        return letter
        print(" ")
    shifted_letter = chr((ord(letter)) + (ord(letter_shift)) - 65)
    if shifted_letter > chr(90):
        new_shifted_letter =  chr((ord(letter)) + (ord(letter_shift)) - 91)
        return new_shifted_letter
        print(new_shifted_letter)
    return shifted_letter
print('SHIFT BY LETTER')
letter = str(input('Enter letter here: '))
letter_shift = str(input('Enter shift letter here: '))
shifted_letter = shift_letter(letter, letter_shift)
print("New letter:",shifted_letter)

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def vigenere_cipher(message, key):
    vigenere_key = key * (len(message) // len(key))
    vigenere_key = vigenere_key + key[:len(message) % len(key)]
    return vigenere_key
def cipher(message,vigenere_key):
    encrypted_message = ''    
    for i in range(len(message)):
        if message[i] == ' ':
            encrypted_message += ' '
        else:
            shift_amount = ord(vigenere_key[i]) - ord('A')
            new_ascii = (ord(message[i]) - ord('A') + shift_amount) % 26
            encrypted_message += chr(new_ascii + ord('A'))
    return encrypted_message
message = str(input('Enter message: '))
key = str(input('Enter key: '))
vigenere_key = vigenere_cipher(message, key)
print('VIGENERE CIPHER')
print('Key phrase:', vigenere_cipher(message, key))
print('Cipher:', cipher(message,vigenere_key))