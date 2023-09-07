import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(maps, x, y):
    if maps[x][y] == 'X':
        return 0
    value = int(maps[x][y])
    maps[x] = maps[x][:y] + 'X' + maps[x][y+1:]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < len(maps) and 0 <= new_y < len(maps[0]):
            value += DFS(maps, new_x, new_y)
    return value

def solution(maps):
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                result = DFS(maps, i, j)
                answer.append(result)
    return sorted(answer) if answer else [-1]
