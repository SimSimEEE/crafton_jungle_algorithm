import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
numbers = [0]*N
result = 0


def perm(cnt, flag):
    if cnt == N:
        global result
        result = max(result,sum([abs(numbers[i]-numbers[i-1]) for i in range(1,N)]))
        return
    else:
        for i in range(N):
            if flag & 1 << i != 0:
                continue
            numbers[cnt] = A[i]
            perm(cnt+1, flag | 1 << i)


perm(0, 0)
print(result)