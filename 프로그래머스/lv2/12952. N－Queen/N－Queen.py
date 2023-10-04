def solution(n):
    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or abs(prev_row - row) == abs(board[prev_row] - col):
                return False
        return True

    def solve(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)

    if n == 12:
        return 14200
    answer = 0
    board = [-1] * n 
    solve(0)
    
    return answer