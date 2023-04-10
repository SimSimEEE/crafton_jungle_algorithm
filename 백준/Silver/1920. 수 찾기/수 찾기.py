import sys
input = sys.stdin.readline


def BS(start, finish, A, B):
    if start > finish:
        return 0

    mid = (finish+start)//2

    if A[mid] == B:
        return 1
    elif A[mid] > B:
        return BS(start, mid-1, A, B)
    else:
        return BS(mid+1, finish, A, B)


N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = map(int, input().split())

for b in B:
    print(BS(0, N-1, A, b))