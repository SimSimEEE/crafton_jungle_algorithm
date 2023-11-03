x, y, c = map(float, input().split())
start = 0
end = min(x, y)
while end - start > 1e-6:
    mid = (start + end) / 2
    d = mid
    h1 = (x ** 2 - d ** 2) ** 0.5
    h2 = (y ** 2 - d ** 2) ** 0.5
    h = (h1 * h2) / (h1 + h2)
    if h > c:
        start = mid
    else:
        end = mid
print('%.3f' % mid)