import sys
input = sys.stdin.readline

def dfs(cnt, sum, add, sub, mul, div):
    global max_result, min_result
    if cnt == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    if add:
        dfs(cnt+1,sum + a[cnt],add-1,sub,mul,div)
    if sub:
        dfs(cnt+1,sum - a[cnt],add,sub-1,mul,div)
    if mul:
        dfs(cnt+1,sum * a[cnt],add,sub,mul-1,div)
    if div:
        dfs(cnt+1,int(sum / a[cnt]),add,sub,mul,div-1)


n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -sys.maxsize
min_result = sys.maxsize

dfs(1, a[0], add, sub, mul, div)

print(max_result)
print(min_result)