def solution(arr):
    def compress(x, y, n):
        if n == 1:
            return [0, 1] if arr[x][y] == 1 else [1, 0]

        all_same = True
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != arr[x][y]:
                    all_same = False
                    break
            if not all_same:
                break

        if all_same:
            return [0, 1] if arr[x][y] == 1 else [1, 0]
        else:
            size = n // 2
            result = [0, 0]

            for i in range(2):
                for j in range(2):
                    quad_result = compress(x + i * size, y + j * size, size)
                    result[0] += quad_result[0]
                    result[1] += quad_result[1]

            return result

    answer = compress(0, 0, len(arr))
    return answer