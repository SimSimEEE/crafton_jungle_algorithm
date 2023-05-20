N, M = map(int, input().split())
A = list(map(int,input().split()))

result = 0
sum_arr = 0
for i in range(N-1):
    sum_arr = A[i]
    if sum_arr == M:
        result += 1
    for j in range(i+1, N):
        sum_arr += A[j]
        if sum_arr == M:
            result += 1
if A[-1] == M:
    result += 1
    
print(result)