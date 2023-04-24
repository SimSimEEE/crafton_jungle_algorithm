import sys
input = sys.stdin.readline

def DFS(cnt, flag):
    if cnt == N-1:
        global max_result,min_result
        tmp = A[0]
        for i in range(N-1):
            if result[i] == 0:
                tmp += A[i+1]
            elif result[i] == 1:
                tmp -= A[i+1]
            elif result[i] == 2:
                tmp *= A[i+1]
            else:
                if tmp > 0:
                    tmp //= A[i+1]
                else:
                    tmp = -((-tmp) // A[i+1])
        max_result = max(max_result, tmp)
        min_result = min(min_result, tmp)
        return
    else:
        for i in range(N-1):
            if flag & 1 << i != 0:
                continue
            result[cnt] = op_list[i]
            DFS(cnt+1, flag | 1 << i)

N = int(input())
A = list(map(int, input().split()))

operator = list(map(int, input().split()))

flag = 0
op_list = []
result = [0]*(N-1)
max_result = -sys.maxsize
min_result = sys.maxsize

for i in range(4):
    for j in range(operator[i]):
        op_list.append(i)

DFS(0,0)

print(max_result)
print(min_result)
