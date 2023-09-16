from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maps, visited, start, end):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < len(maps) and 0 <= newY < len(maps[0]) and visited[newX][newY] == 0:
                if maps[newX][newY] != "X":
                    visited[newX][newY] = visited[x][y] + 1
                    queue.append((newX, newY))

def getXY(maps, flag):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == flag:
                return i, j

def solution(maps):
    answer = 0
    visited = [[0]* len(maps[0]) for _ in range(len(maps))]
    startX, startY = getXY(maps, "S")
    switchX, switchY = getXY(maps, "L")
    endX, endY = getXY(maps, "E")
    bfs(maps, visited, (startX, startY), (switchX, switchY))
    if visited[switchX][switchY] == 0:
        return -1
    answer += visited[switchX][switchY]
    visited = [[0]* len(maps[0]) for _ in range(len(maps))]
    bfs(maps, visited, (switchX, switchY), (endX, endY))
    if visited[endX][endY] == 0:
        return -1
    answer += visited[endX][endY]
    return answer

