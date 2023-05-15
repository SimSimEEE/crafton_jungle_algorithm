def solution(maps):
    answer = 0
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    queue = [(0, 0 , 1)]
    while queue:
        row, col, answer = queue.pop(0)
        if row == n-1 and col == m-1:
            return answer
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < m:
                if maps[nrow][ncol] == 1:
                    maps[nrow][ncol] = 0
                    queue.append((nrow, ncol, answer + 1))
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return answer