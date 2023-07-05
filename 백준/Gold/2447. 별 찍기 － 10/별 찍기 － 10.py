n = int(input())
graph = [['*'] * n for _ in range(n)]


def delete_star(n, x, y):
    if n == 1:
        return

    third = n // 3
    for i in range(x + third, x + 2 * third):
        for j in range(y + third, y + 2 * third):
            graph[i][j] = " "

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                delete_star(third, x + i * third, y + j * third)


delete_star(n, 0, 0)
for row in graph:
    print(''.join(row))