import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cal_nums = list(map(int, input().split()))


def upside_down(a):
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


def left_right(a):
    for i in range(n):
        for j in range(m//2):
            a[i][j], a[i][m-j-1] = a[i][m-j-1], a[i][j]


def right_rotate90(a):
    global n, m
    n, m = m, n
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[m-j-1][i]
    return b


def left_rotate90(a):
    global n, m
    n, m = m, n
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[j][n-i-1]
    return b

def quadrant_right_rotate(a):
    for i in range(n//2):
        for j in range(m//2):
            a[i][j], a[i+n//2][j], a[i][j+m//2], a[i+n//2][j+m//2] = a[i+n//2][j], a[i+n//2][j+m//2], a[i][j], a[i][j+m//2]

def quadrant_left_rotate(a):
    for i in range(n//2):
        for j in range(m//2):
            a[i][j], a[i+n//2][j], a[i][j+m//2], a[i+n//2][j+m//2] = a[i][j+m//2], a[i][j], a[i+n//2][j+m//2], a[i+n//2][j]
            
for cal_num in cal_nums:
    if cal_num == 1:
        upside_down(a)
    elif cal_num == 2:
        left_right(a)
    elif cal_num == 3:
        a = right_rotate90(a)
    elif cal_num == 4:
        a = left_rotate90(a)
    elif cal_num == 5:
        quadrant_right_rotate(a)
    elif cal_num == 6:
        quadrant_left_rotate(a)

for i in a:
    for j in i:
        print(j, end=' ')
    print()