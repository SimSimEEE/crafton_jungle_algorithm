n = int(input())
h = list(map(int, input().split()))
h.sort(reverse=True)
answer = float('inf')
for i in range(n - 3):
    for j in range(i + 3, n):
        l, r = i + 1, j - 1
        while l < r:
            s = h[i] + h[j] - h[l] - h[r]
            answer = min(answer, abs(s))
            if s < 0:
                l += 1
            else:
                r -= 1
print(answer)