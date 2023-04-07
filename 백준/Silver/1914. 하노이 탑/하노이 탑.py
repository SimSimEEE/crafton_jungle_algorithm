import sys
input = sys.stdin.readline
def hanoi(frm, to, N):
    if N == 1:
        print(*[frm, to])
    else:
        empty = 6 - frm - to
        hanoi(frm, empty, N-1)
        print(*[frm, to])
        hanoi(empty, to, N-1)
N = int(input())
print(2**N-1)
if N <=20:
    hanoi(1, 3, N)