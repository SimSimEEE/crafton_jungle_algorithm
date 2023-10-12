import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
cake = [int(input()) for _ in range(m)] + [l]


def isPossible(mid):
    left = 0
    cnt = 0
    for right in cake:
        if right - left >= mid:
            left = right
            cnt += 1
    return cnt > friend

for _ in range(n):
    friend = int(input())
    start = 1
    end = l
    answer = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        if isPossible(mid):
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
    print(answer)
