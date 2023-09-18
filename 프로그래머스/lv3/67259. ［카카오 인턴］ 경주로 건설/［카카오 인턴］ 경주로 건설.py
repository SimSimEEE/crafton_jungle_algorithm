def dfs(x, y, direction, cost, board, visit, n, dx, dy):
    if board[x][y] or visit[x][y] or x == y == n - 1:
        return

    visit[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if direction == 'x':
            if 0 <= nx < n and board[nx][y] == 0 and not visit[nx][y]:
                new_cost = cost[x][y] + 100
                if new_cost < cost[nx][y]:
                    cost[nx][y] = new_cost
                    visit[nx][y] = False
                    dfs(nx, y, 'x', cost, board, visit, n, dx, dy)
                    visit[nx][y] = False

            if 0 <= ny < n and board[x][ny] == 0 and not visit[x][ny]:
                new_cost = cost[x][y] + 600
                if new_cost < cost[x][ny]:
                    cost[x][ny] = new_cost
                    visit[x][ny] = False
                    dfs(x, ny, 'y', cost, board, visit, n, dx, dy)
                    visit[x][ny] = False

        else:
            if 0 <= ny < n and board[x][ny] == 0 and not visit[x][ny]:
                new_cost = cost[x][y] + 100
                if new_cost < cost[x][ny]:
                    cost[x][ny] = new_cost
                    visit[x][ny] = False
                    dfs(x, ny, 'y', cost, board, visit, n, dx, dy)
                    visit[x][ny] = False

            if 0 <= nx < n and board[nx][y] == 0 and not visit[nx][y]:
                new_cost = cost[x][y] + 600
                if new_cost < cost[nx][y]:
                    cost[nx][y] = new_cost
                    visit[nx][y] = False
                    dfs(nx, y, 'x', cost, board, visit, n, dx, dy)
                    visit[nx][y] = False


def solution(board):
    answer = 10**7
    n = len(board)

    for k in range(2):
        cost = [[float('inf')] * n for _ in range(n)]
        cost[0][0] = 0
        if not board[0][1]:
            cost[0][1] = 100
        if not board[1][0]:
            cost[1][0] = 100
        visit = [[False] * n for _ in range(n)]

        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]  # Right, Down, Up, Left

        if k:
            if not board[0][1]:
                dfs(0, 1, 'y', cost, board, visit, n, dx, dy)
        else:
            if not board[1][0]:
                dfs(1, 0, 'x', cost, board, visit, n, dx, dy)

        answer = min(cost[n - 1][n - 1], answer)
        print(*cost, sep='\n', end='\n\n')
    return answer
