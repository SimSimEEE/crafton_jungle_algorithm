import sys

def dfs(cnt, flag, tmp):
    global max_result, min_result
    if cnt == n - 1:
        max_result = max(max_result, tmp)
        min_result = min(min_result, tmp)
    else:
        for i in range(n - 1):
            if flag & (1 << i):
                continue
            new_tmp = tmp
            if op_list[i] == 0:
                new_tmp += a[cnt + 1]
            elif op_list[i] == 1:
                new_tmp -= a[cnt + 1]
            elif op_list[i] == 2:
                new_tmp *= a[cnt + 1]
            else:
                if new_tmp > 0:
                    new_tmp //= a[cnt + 1]
                else:
                    new_tmp = -((-new_tmp) // a[cnt + 1])
            dfs(cnt + 1, flag | (1 << i), new_tmp)

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

op_list = [i for i in range(4) for _ in range(op[i])]
max_result = -sys.maxsize
min_result = sys.maxsize
dfs(0, 0, a[0])

print(max_result)
print(min_result)