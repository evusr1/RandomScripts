# SkillsForAll
# Python Essentials 2 - 4.3.8 LAB
# Character Frequency Histogram


#test file generation
sfile = open("samplefile.txt", "wt")
sfile.write("BaBc")
sfile.close()

fn = input("Enter a file name to generate a Character Frequency histogram for:")

letters= {}

try:
    for text in open(fn, "rt"):
        for c in text:
            letter = c.lower()
            
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
except Exception as e:
    print(e)

for letter in sorted(letters.items()):
    print(letter[0], "->", letter[1])
