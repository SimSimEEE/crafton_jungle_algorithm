import sys
input = sys.stdin.readline

white, blue = 0, 0
def NxN(arr):
    global white, blue
    N = len(arr)
    if all([0 not in i for i in arr]):
        blue += 1
    elif all([1 not in i for i in arr]):
        white += 1
    else:
        NxN([row[0:N//2] for row in arr[0:N//2]])
        NxN([row[N//2:N] for row in arr[0:N//2]])
        NxN([row[0:N//2] for row in arr[N//2:N]])
        NxN([row[N//2:N] for row in arr[N//2:N]])
    return
N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
NxN(field)
print(white,blue,sep="\n")