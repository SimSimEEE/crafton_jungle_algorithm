import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def sol(A,B,C):
    if B == 1:
        return A%C
    elif B%2 == 0:
        return (sol(A,B//2,C)**2)%C
    else:
        return (sol(A,B//2,C)**2*A)%C

print(sol(A,B,C))