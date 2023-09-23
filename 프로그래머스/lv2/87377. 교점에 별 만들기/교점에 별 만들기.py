from itertools import combinations

def getMeet(a, b):
    A, B, E = a
    C, D, F = b
    parent = A*D - B*C
    if parent != 0:
        x = (B*F - E*D) / parent
        y = (E*C - A*F) / parent
        return x, y

def solution(line):
    answer = []
    points = []
    minX, minY, maxX, maxY = float("inf"), float("inf"), float("-inf"), float("-inf")
    for a, b in combinations(line, 2):
        point = getMeet(a, b)
        if point and point[0].is_integer() and point[1].is_integer():
            minX, minY = min(minX, point[0]), min(minY, point[1]) 
            maxX, maxY = max(maxX, point[0]), max(maxY, point[1])
            points.append(point)
    
    rows = int(maxY - minY + 1)
    cols = int(maxX - minX + 1)
    
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    
    for point in points:
        x, y = int(point[0] - minX), int(point[1] - minY)
        grid[y][x] = '*'
    
    grid_str = [''.join(row) for row in grid]
    
    return grid_str[::-1]