# SkillsForAll
# Python Essentials 2 -2.5.7 LAB
# Palindrome

def is_palindrome(text):
    text = text.upper().replace(" ", "")
    
    if len(text) < 1:
        return False
    
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            return False
    
    return True
    
text = input("Enter text: ")

if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")


  # Post Notes: You can just reverse the string by using text[::-1]
