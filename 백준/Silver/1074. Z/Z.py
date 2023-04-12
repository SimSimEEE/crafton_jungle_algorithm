import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

def Z(N, r, c):
    N //= 2
    if N == 0:
        return 0
    xy = 2*(r//N) + c//N
    return N*N * xy + Z(N, r-N*(r//N), c-N*(c//N))

print(Z(2**N, r, c))