# SkillsForAll
# Python Essentials 2 - 2.5.9 LAB
# The Digit of Life

bday = input("What is your birthday date YYYYMMDD, YYYYDDMM, or MMDDYYYY?")


while int(bday) > 9:
    bday_sum = 0
    for digit in bday:
        bday_sum += int(digit)
    
    bday = str(bday_sum)

print(bday)
