import sys
input = sys.stdin.readline

N = int(input())
board = [-1] * N 
def promise(row, col):
    for i in range(row):
        if (board[i] == col) or (board[i] - i == col - row) or (board[i] + i == col + row):
            return False
    return True

def n_queen(row):
    if row == N: 
        return 1
    
    count = 0
    for col in range(N):
        if promise(row, col): 
            board[row] = col  
            count += n_queen(row + 1) 
            board[row] = -1 
    return count

print(n_queen(0))
