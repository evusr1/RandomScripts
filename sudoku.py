# SkillsForAll
# Python Essentials 2 -2.5.11 LAB
# Sudoku Validator

board_row = 9
board_col = 9

def validate_sudoku(board):
    cols = [[] for y in range(board_row)]
    sectors = [[] for i in range((board_row // 3) * (board_col // 3))]
    
    for row in range(len(board)):
        for i in range(1,10):
            if i not in board[row]:
                return False
                
        for col in range(board_row):
            cols[col].append(board[row][col])
            sectors[(row // 3) * (board_row // 3) + col // 3].append(board[row][col])
    
    for col in cols:
        for i in range(1,10):
            if i not in col:
                return False
                
    for sector in sectors:
        for i in range(1,10):
            if i not in sector:
                return False
    
    return True
    
board_input = []

while len(board_input) < board_row * board_col:
    number_input = input("Enter board numbers:")
    
    for n in number_input:
        if n.isdigit() and len(board_input) < board_row * board_col:
            board_input.append(int(n))
            
board = [[board_input[board_row * y + x] for x in range(board_col)] for y in range(board_row)]

print()

if validate_sudoku(board):
    print("Yes")
else:
    print("No")
