# SkillsForAll
# Python Essentials 2 - 2.5.6 LAB
# Caesar Cipher Lab

def caesar_cipher(text, shift):
    result = ""
    for letter in text:
        if not letter.isalpha():
            result += letter
            continue
        
        letter_code = ord(letter)
        
        range_start = ord('a')
        range_end = ord('z') - range_start + 1
        
        if letter.isupper():
            range_start = ord('A')

        result += chr(range_start + (letter_code + shift - range_start) % range_end)
        
    return result

text = input("Enter text to encrypt:")
shift = int(input("Enter a number to shift letters:"))

while shift not in range(1, 26):
    shift = int(input("Enter a number to shift letters:"))

print(caesar_cipher(text, shift))
