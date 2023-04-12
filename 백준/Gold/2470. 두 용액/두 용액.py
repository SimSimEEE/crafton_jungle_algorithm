import sys
input = sys.stdin.readline
N = int(input())
X = sorted(map(int, input().split()))
nearzero = sys.maxsize
start, end = 0, N-1
result_i, result_j = 0,0
if N == 2:
    print(*X)
else:
    while start < end:
        sum = X[end] + X[start]
        if abs(sum) < nearzero:
            nearzero = abs(sum)
            result_i = start
            result_j = end
            if sum == 0:
                break
        else:
            if sum > 0:
                end-=1
            else:
                start+=1
    
    print(X[result_i],X[result_j])