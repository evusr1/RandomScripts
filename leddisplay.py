# SkillsForAll
# Python Essentials 2 - 2.4.6 LAB
# LED Display Lab

def to_digit(digit):
    digits = [
        [
            "###",
            "# #",
            "# #",
            "# #",
            "###",
        ],
        [
            "  #",
            "  #",
            "  #",
            "  #",
            "  #",
        ],
        [
            "###",
            "  #",
            "###",
            "#  ",
            "###",
        ],
        [
            "###",
            "  #",
            "###",
            "  #",
            "###",
        ],
        [
            "# #",
            "# #",
            "###",
            "  #",
            "  #",
        ],
        [
            "###",
            "#  ",
            "###",
            "  #",
            "###",
        ],
        [
            "###",
            "#  ",
            "###",
            "# #",
            "###",
        ],
        [
            "###",
            "  #",
            "  #",
            "  #",
            "  #",
        ],
        [
            "###",
            "# #",
            "###",
            "# #",
            "###",
        ],
        [
            "###",
            "# #",
            "###",
            "  #",
            "###",
        ]
    ]
    
    return digits[digit]
    
def strnum_to_digits(strnum):
    digit_str_list = []
    
    for digit in strnum:
        if not digit.isdigit():
            if not len(digit_str_list):
                return
            break
        digit_str_list.append(to_digit(int(digit)))
    
    for line in range(5):
        for digit_string in digit_str_list:
            print(digit_string[line], end = " ")
        print()
        

strnum_to_digits(input("Enter a number:"))
