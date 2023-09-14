def rotation(arr, query):
    x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    prev = arr[x1][y1]
    min_val = prev

    for y in range(y1 + 1, y2 + 1):
        curr = arr[x1][y]
        arr[x1][y] = prev
        prev = curr
        min_val = min(min_val, curr)

    for x in range(x1 + 1, x2 + 1):
        curr = arr[x][y2]
        arr[x][y2] = prev
        prev = curr
        min_val = min(min_val, curr)

    for y in range(y2 - 1, y1 - 1, -1):
        curr = arr[x2][y]
        arr[x2][y] = prev
        prev = curr
        min_val = min(min_val, curr)

    for x in range(x2 - 1, x1 - 1, -1):
        curr = arr[x][y1]
        arr[x][y1] = prev
        prev = curr
        min_val = min(min_val, curr)

    return min_val


def solution(rows, columns, queries):
    arr = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    answer = []
    for query in queries:
        min_val = rotation(arr, query)
        answer.append(min_val)

    return answer
