while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i]
                                  [j - 1], board[i - 1][j - 1]) + 1
    print(max([max(row) for row in board]))