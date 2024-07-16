# SkillsForAll
# Python Essentials 2 - 2.4.8 LAB
# Anagrams

def isanagram(text, to_check):
    to_check = to_check.upper().replace(" ", "")
    text = text.upper().replace(" ", "")
    
    if len(text) < 1 or len(to_check) < 1:
        return False
    
    if len(text) != len(to_check):
        return False
    
    for letter in text:
         next_text = to_check.replace(letter, "", 1)
         if len(next_text) == len(text):
            return False
    
    return True
    
text = input("Enter text 1:")
to_check = input("Enter text 2:")


if isanagram(text, to_check):
    print("Anagrams")
else:
    print("Not anagrams")
