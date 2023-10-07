def solution(board, skill):
    answer = 0
    pre_fix = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for Type, r1, c1, r2, c2, degree in skill:
        if Type == 1:
            degree = -degree
        pre_fix[r1][c1] += degree
        pre_fix[r1][c2+1] += -degree
        pre_fix[r2+1][c1] += -degree
        pre_fix[r2+1][c2+1] += degree
        
    for i in range(len(pre_fix)):
        for j in range(1, len(pre_fix[0])):
            pre_fix[i][j] += pre_fix[i][j - 1]
            
    for j in range(len(pre_fix[0])):
        for i in range(1, len(pre_fix)):
            pre_fix[i][j] += pre_fix[i - 1][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + pre_fix[i][j] > 0:
                answer += 1
                
    return answer