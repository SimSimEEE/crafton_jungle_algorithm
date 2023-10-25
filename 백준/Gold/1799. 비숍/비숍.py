n = int(input())
chessboard = [list(map(int, input().split())) for _ in range(n)]
white, black = [], []

for i in range(n):
    for j in range(n):
        if chessboard[i][j] == 1:
            if (i + j) % 2 == 0:
                white.append((i, j))
            else:
                black.append((i, j))

def can_place_bishop(bishops, x, y):
    for i, j in bishops:
        if abs(x - i) == abs(y - j):
            return False
    return True

def find_max_bishops(bishop_list):
    max_bishops = 0

    def recursion(idx, bishops):
        nonlocal max_bishops
        if idx == len(bishop_list):
            max_bishops = max(max_bishops, len(bishops))
            return
        x, y = bishop_list[idx]
        if can_place_bishop(bishops, x, y):
            bishops.append((x, y))
            recursion(idx + 1, bishops)
            bishops.pop()
        recursion(idx + 1, bishops)

    recursion(0, [])
    return max_bishops

max_white_bishops = find_max_bishops(white)
max_black_bishops = find_max_bishops(black)
answer = max_white_bishops + max_black_bishops
print(answer)
