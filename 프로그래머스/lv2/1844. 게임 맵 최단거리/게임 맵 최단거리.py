def solution(maps):
    answer = 0
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < m:
                if maps[nrow][ncol] == 1:
                    maps[nrow][ncol] = maps[row][col] + 1
                    queue.append((nrow, ncol))
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]