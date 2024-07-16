# SkillsForAll
# Python Essentials 2 - 2.5.10 LAB
# Find Word

def find_word(haystack, needle):
    haystack = haystack.upper()
    needle = needle.upper()
    
    for s in needle:
        s_pos = haystack.find(s)
        
        if s_pos < 0:
            return False
            
        haystack = haystack[s_pos + 1:]

    return True
    
needle = input("Enter a word to find: ")
haystack = input("Enter where to find it: ")

if find_word(haystack, needle):
    print("Yes")
else:
    print("No")
