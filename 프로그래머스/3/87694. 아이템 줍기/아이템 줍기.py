from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    coordinates = set()
    answer = 0
    for x1,y1,x2,y2 in rectangle:
        coordinates.update([(j+0.5, i) for j in range(y1, y2) for i in (x1, x2)])
        coordinates.update([(j,i+0.5) for i in range(x1, x2) for j in (y1, y2)])
    
    outskirts = set()
    for y, x in coordinates:
        if all(not (x1 < x < x2 and y1 < y < y2) for x1, y1, x2, y2 in rectangle):
            outskirts.add((x, y))
    
    queue = deque([(characterX, characterY, 0)])
    dx = [0, 0, 0.5, -0.5]
    dy = [0.5, -0.5, 0, 0]
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == itemX and y == itemY:
            return cnt
        for i in range(4):
            if (newX := x + dx[i], newY := y + dy[i]) in outskirts:
                outskirts.remove((newX, newY))
                queue.append((x + dx[i]*2, y + dy[i]*2, cnt+1))