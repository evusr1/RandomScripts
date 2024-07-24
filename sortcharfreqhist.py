# SkillsForAll
# Python Essentials 2 - 4.3.9 LAB
# Sorted Character Frequency Histogram

from pathlib import Path

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

out_fn = Path(fn).stem + ".hist"
out = open(out_fn, "wt")

for letter in sorted(letters.items(), key=lambda x: x[1], reverse=True):
    out.write(str(letter[0]) + " -> " + str(letter[1]) + "\n")

out.close()
