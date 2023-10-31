import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def rotate_layer(matrix, layer):
    rows = len(matrix)
    cols = len(matrix[0])
    top, left = layer, layer
    bottom, right = rows - layer - 1, cols - layer - 1

    rotations = r % (2 * (bottom - top + 1) + 2 * (right - left + 1) - 4)

    for _ in range(rotations):
        temp = matrix[top][left]

        # Move elements in the top row
        for j in range(left, right):
            matrix[top][j] = matrix[top][j + 1]

        # Move elements in the right column
        for i in range(top, bottom):
            matrix[i][right] = matrix[i + 1][right]

        # Move elements in the bottom row
        for j in range(right, left, -1):
            matrix[bottom][j] = matrix[bottom][j - 1]

        # Move elements in the left column
        for i in range(bottom, top, -1):
            matrix[i][left] = matrix[i - 1][left]

        matrix[top + 1][left] = temp


for layer in range(min(n, m) // 2):
    rotate_layer(a, layer)

for i in a:
    for j in i:
        print(j, end=' ')
    print()
