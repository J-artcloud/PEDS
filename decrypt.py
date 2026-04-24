##decrypt function
def decrypt (ciphertext, shift):
    decrypted_text = " "
    for char in ciphertext:
        if char .isalpha(): 
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char)) -shift_base - shift[] % 26 + shift_base)
            decrypted_text +=
    decrypted_char
            else:
                    decrypted_text += char 
             
             return decryipted_text 
                
        