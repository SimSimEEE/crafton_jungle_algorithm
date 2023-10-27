import sys
input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
paper_cnt = [0, 0, 0]


def check(x, y, n):
    global paper_cnt
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        check(x + k * n // 3, y + l * n // 3, n // 3)
                return
    paper_cnt[color + 1] += 1


check(0, 0, n)
for i in paper_cnt:
    print(i)
