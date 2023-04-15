import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

def Z(N, r, c):
    if N == 0:
        return 0
    return N*N * (2*(r//N) + c//N) + Z(N//2, r-N*(r//N), c-N*(c//N))

print(Z(2**(N-1), r, c))